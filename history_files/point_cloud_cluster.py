import numpy as np
import open3d

pcdraw = np.fromfile('/media/lzy/14BA7CD7BA7CB6B8/lzy_2022/DataSets/KITTI/gt_database/000043_Pedestrian_2.bin', dtype=np.float32, count=-1).reshape([-1, 4])[:, :3]
print(pcdraw.shape)
np.savetxt('/media/lzy/14BA7CD7BA7CB6B8/lzy_2022/subt_person/available-tools/000043_Pedestrian_2.txt', pcdraw, fmt='%f')

copcd = pcdraw
print(copcd[:, 2])
x = copcd[:, 0]
y = copcd[:, 1]
z = copcd[:, 2]
# z.sort()
print(z.shape)
# z is the height of the point cloud with shape (n, 1), now cluster the point cloud with height

tanz = z/(np.sqrt(x*x + y*y))
# tanz.sort()
print(tanz)


pcd = open3d.geometry.PointCloud()
pcd.points = open3d.utility.Vector3dVector(pcdraw)
vis = open3d.visualization.Visualizer()
vis.create_window()	#创建窗口
# vis.register_animation_callback(rotate_view)
render_option: open3d.visualization.RenderOption = vis.get_render_option()	#设置点云渲染参数
render_option.background_color = np.array([0,0,0])	#设置背景色（这里为黑色）
render_option.point_size = 4	#设置渲染点的大小
vis.add_geometry(pcd)	#添加点云
# 坐标系
# vis.add_geometry(open3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0, origin=[0, 0, 0]))

vis.run()


