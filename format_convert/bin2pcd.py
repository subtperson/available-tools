# coding=utf-8
# 将KITTI的bin格式点云转换为pcd格式，并可视化

import numpy as np
import struct
import open3d

size_float = 4
list_pcd = []
with open('/media/lzy/14BA7CD7BA7CB6B8/lzy_2022/subt_person/ST3D/data/kitti/training/velodyne/000073.bin', "rb") as f:
    byte = f.read(size_float * 4)
    while byte:
        x, y, z, intensity = struct.unpack("ffff", byte)
        list_pcd.append([x, y, z, intensity])
        byte = f.read(size_float * 4)
np_pcd = np.asarray(list_pcd)

# np_pcd = np.load('/media/lzy/14BA7CD7BA7CB6B8/lzy_2022/DataSets/jrdb2kitti/training/velodyne/000005.npy')
# np_pcd = np_pcd[:, :3]



# print(np_pcd.shape)
np_pcd = np_pcd[4:]  # Edgar数据集的一些场景，前几个点数据不对，删去，要不影响可视化
print(np_pcd[0:30,3])

# np_pcd[:, 2] = 0   
# limit z axis < 1 and > -1
np_pcd = np_pcd[np_pcd[:, 2] > -2.2]
np_pcd = np_pcd[np_pcd[:, 2] < 0.6]



pcd = open3d.geometry.PointCloud()


# in np_pcd, the first three columns are x,y,z, the last column is color of the point
pcd.points = open3d.utility.Vector3dVector(np_pcd[:, 0:3])
# color from 1 channel to 3 channels
# color = np_pcd[:, 3:4]
# color = np.concatenate((color, color, color), axis=1)

# pcd.colors = open3d.utility.Vector3dVector(color)
# pcd.colors = open3d.utility.Vector3dVector()

# 点云颜色
# pcd.paint_uniform_color([1,1,1])




# 旋转
def rotate_view(vis):
    ctr = vis.get_view_control()
    ctr.rotate(10.0, 0.0)
    return False

# 方法1
# open3d.visualization.draw_geometries_with_animation_callback([pcd], rotate_view)

# 方法2
vis = open3d.visualization.Visualizer()
vis.create_window()	#创建窗口
# vis.register_animation_callback(rotate_view)
render_option: open3d.visualization.RenderOption = vis.get_render_option()	#设置点云渲染参数
render_option.background_color = np.array([0,0,0])	#设置背景色（这里为黑色）
render_option.point_size = 1	#设置渲染点的大小
vis.add_geometry(pcd)	#添加点云
# 坐标系
vis.add_geometry(open3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0, origin=[0, 0, 0]))

vis.run()

# 保存pcd
# open3d.io.write_point_cloud('1644609772_916356000.pcd', pcd, write_ascii=False, compressed=False, print_progress=False)
