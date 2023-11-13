import open3d as o3d
import numpy as np
import os
import struct


path = "/media/lzy/14BA7CD7BA7CB6B8/lzy_2022/subt_person/ST3D/data/edgar/training/velodyne/"
pcfile = os.listdir(path)
# sort by index(000000.bin, 000001.bin, ...)
pcfile.sort(key=lambda x: int(x[:-4]))
# pcfile = pcfile[1:2]

save_path = "/media/lzy/14BA7CD7BA7CB6B8/lzy_2022/subt_person/ST3D/data/edgar/training/velodyne_filter/"
if not os.path.exists(save_path):
    os.makedirs(save_path)


for i in pcfile:
    size_float = 4
    list_pcd = []
    # with open('C:\\Users\\lance\\Desktop\\GoogleDrive\\codes\\demo\\data\\kitti\\kitti_000008.bin', "rb") as f:
    with open(path+i, "rb") as f:
        byte = f.read(size_float * 4)
        while byte:
            x, y, z, intensity = struct.unpack("ffff", byte)
            list_pcd.append([x, y, z, intensity])
            byte = f.read(size_float * 4)
    np_pcd = np.asarray(list_pcd)[8:]  # Edgar数据集的一些场景，前几个点数据不对，删去，要不影响可视化
    # print(np_pcd.shape)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np_pcd[:, 0:3])


    num_neighbors = 20  # K邻域点的个数
    std_ratio = 2  # 标准差乘数
    # 执行统计滤波，返回滤波后的点云sor_pcd和对应的索引ind
    sor_pcd, ind = pcd.remove_statistical_outlier(num_neighbors, std_ratio)
    index = np.asarray(ind)
    # print('index', index.shape)
    points_filter = np_pcd[index]
    print(i, 'filter-points:', np_pcd.shape[0] - points_filter.shape[0])
    points_filter.astype(np.float32).tofile(save_path+i)




    # sor_pcd.paint_uniform_color([1,1,1])
    # sor_noise_pcd = pcd.select_by_index(ind, invert=True)
    # sor_noise_pcd.paint_uniform_color([0,1,0])

    # vis = o3d.visualization.Visualizer()
    # vis.create_window()	#创建窗口
    # # vis.register_animation_callback(rotate_view)
    # render_option: o3d.visualization.RenderOption = vis.get_render_option()	#设置点云渲染参数
    # render_option.background_color = np.array([0,0,0])	#设置背景色（这里为黑色）
    # render_option.point_size = 1	#设置渲染点的大小
    # vis.add_geometry(sor_pcd)	#添加点云
    # vis.add_geometry(sor_noise_pcd)
    # vis.run()







