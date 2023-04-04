import numpy as np
import open3d


# points = np.fromfile('C:\\Users\\lance\\Desktop\\n008-2018-05-21-11-06-59-0400__RADAR_FRONT__1526915244547859.pcd', dtype=np.float32, count=-1, ).reshape([-1, 4])
# print(points.shape)


pcd = open3d.io.read_point_cloud('C:\\Users\\lance\\Desktop\\n008-2018-05-21-11-06-59-0400__RADAR_FRONT__1526915244547859.pcd')
open3d.visualization.draw_geometries([pcd])

