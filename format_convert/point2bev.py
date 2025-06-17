#coding=utf-8
# 将点云转换为bev鸟瞰视图，根据点密度赋予颜色
# 2023.6.7 lzy
import os

import numpy
import numpy as np
from PIL import Image
import struct
import matplotlib.pyplot as plt

def p2bev(p_path, bev_path):
    # 1.读取点云数据
    size_float = 4
    list_pcd = []
    with open(p_path, "rb") as f:
        byte = f.read(size_float * 4)
        while byte:
            x, y, z, intensity = struct.unpack("ffff", byte)
            list_pcd.append([x, y, z])
            byte = f.read(size_float * 4)
    np_pcd = np.asarray(list_pcd)
    print(np_pcd.shape)

    # 2.将点云投影到bev平面
    # 设置鸟瞰图范围
    side_range = (-35, 35)  # 左右距离
    fwd_range = (0, 35)  # 后前距离


    x_points = np_pcd[:, 0]
    y_points = np_pcd[:, 1]
    z_points = np_pcd[:, 2]

    # 过滤掉不在范围内的点
    f_filt = np.logical_and(x_points > fwd_range[0], x_points < fwd_range[1])
    s_filt = np.logical_and(y_points > side_range[0], y_points < side_range[1])
    filter = np.logical_and(f_filt, s_filt)
    indices = np.argwhere(filter).flatten()
    x_points = x_points[indices]
    y_points = y_points[indices]
    z_points = z_points[indices]

    res = 0.05003  # 分辨率
    x_img = (-y_points / res ).astype(np.int32)
    y_img = (-x_points / res ).astype(np.int32)
    # 调整坐标原点
    x_img -= int(np.floor(side_range[0]) / res)
    y_img += int(np.floor(fwd_range[1]) / res)
    print(x_img.min(), x_img.max(), y_img.min(), x_img.max())

    # 填充像素值
    height_range = (-3, 1)
    pixel_value = np.clip(a=z_points, a_max=height_range[1], a_min=height_range[0])


    def scale_to_255(a, min, max, dtype=np.uint8):
        return ((a - min) / float(max - min) * 255).astype(dtype)


    pixel_value = scale_to_255(pixel_value, height_range[0], height_range[1])

    # 创建图像数组
    x_max = 1 + int((side_range[1] - side_range[0]) / res)
    y_max = 1 + int((fwd_range[1] - fwd_range[0]) / res)
    im = np.zeros([y_max, x_max], dtype=np.uint8)
    im[y_img, x_img] = pixel_value

    # imshow （灰度）
    # im2 = Image.fromarray(im)
    # im2.show()

    # imshow （彩色）
    plt.imsave(bev_path, im, cmap="nipy_spectral", vmin=0, vmax=255)
    # plt.imshow(im, cmap="nipy_spectral", vmin=0, vmax=255)
    # plt.show()

if __name__ == '__main__':

    p_path = '/media/gty/14BA7CD7BA7CB6B8/lzy_2022/subt_person/ST3D/data/kitti/training/velodyne'
    bev_path = '/media/gty/14BA7CD7BA7CB6B8/lzy_2022/subt_person/ST3D/data/kitti/training/bev'
    #bev folder is exist?
    if not os.path.exists(bev_path):
        os.makedirs(bev_path)
    split_path = '/media/gty/14BA7CD7BA7CB6B8/lzy_2022/subt_person/ST3D/data/kitti/ImageSets/trainval.txt'
    pclist = numpy.loadtxt(split_path, dtype=str).tolist()
    print(len(pclist))
    print(pclist)
    for pcname in pclist:
        print(pcname+'.bin')
        p2bev(os.path.join(p_path, pcname+'.bin'), os.path.join(bev_path, pcname+'.png'))