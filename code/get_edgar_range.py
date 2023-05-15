#coding=utf-8
import numpy as np
import struct
import open3d

size_float = 4
list_pcd = []
all = []
# with open('C:\\Users\\lance\\Desktop\\GoogleDrive\\codes\\demo\\data\\kitti\\kitti_000008.bin', "rb") as f:
for i in range(1001,1300):
    with open('C:\\Users\\lance\\Desktop\\subtperson\\edgar\\training\\velodyne\\00{}.bin'.format(i), "rb") as f:
        byte = f.read(size_float * 4)
        while byte:
            x, y, z, intensity = struct.unpack("ffff", byte)
            list_pcd.append([x, y, z])
            byte = f.read(size_float * 4)
    np_pcd = np.asarray(list_pcd)
    # print(np_pcd.shape)
    np_pcd = np_pcd[4:]  # Edgar数据集的一些场景，前几个点数据不对，删去，要不影响可视化
    # print(np_pcd.shape)
    juzhen = np.asarray([min(np_pcd[:,0]), max(np_pcd[:,0]), min(np_pcd[:,1]), max(np_pcd[:,1]), min(np_pcd[:,2]), max(np_pcd[:,2])])
    print(juzhen)
    all.append(juzhen)

pass
