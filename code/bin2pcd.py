#coding=utf-8
# 将KITTI的bin格式点云转换为pcd格式，并可视化

import numpy as np
import struct
import open3d


size_float = 4
list_pcd = []
with open('C:\\Users\\lance\\Desktop\\GoogleDrive\\codes\\demo\\data\\kitti\\kitti_000008.bin', "rb") as f:
# with open('C:\\Users\\lance\\Desktop\\edgar\\training\\velodyne\\000008.bin', "rb") as f:
    byte = f.read(size_float * 4)
    while byte:
        x, y, z, intensity = struct.unpack("ffff", byte)
        list_pcd.append([x, y, z])
        byte = f.read(size_float * 4)
np_pcd = np.asarray(list_pcd)
print(np_pcd.shape)
np_pcd = np_pcd[4:]  #Edgar数据集的一些场景，前几个点数据不对，删去，要不影响可视化
pcd = open3d.geometry.PointCloud()
pcd.points = open3d.utility.Vector3dVector(np_pcd)

#点云颜色
pcd.paint_uniform_color([1,0.706,0])

# 方法1
# open3d.visualization.draw_geometries([pcd])


# 方法2
vis = open3d.visualization.Visualizer()
vis.create_window()	#创建窗口
render_option: open3d.visualization.RenderOption = vis.get_render_option()	#设置点云渲染参数
render_option.background_color = np.array([0, 0, 0])	#设置背景色（这里为黑色）
render_option.point_size = 1.0	#设置渲染点的大小
vis.add_geometry(pcd)	#添加点云
vis.run()

# 保存pcd
# open3d.io.write_point_cloud('1644609772_916356000.pcd', pcd, write_ascii=False, compressed=False, print_progress=False)
