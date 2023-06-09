import os
import numpy as np
import sys

lidar_dir = 'C:\\Users\\lance\\Desktop\\subtperson\\edgar\\training\\velodyne'
save_dir = 'C:\\Users\\lance\\Desktop\\subtperson\\edgar\\training\\velodyne_edited'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

def load_velo_scan(velo_filename):
    scan = np.fromfile(velo_filename, dtype=np.float32)
    scan = scan.reshape((-1, 4))
    print(scan)
    return scan


for x in os.listdir(lidar_dir):
    print(x)
    lidar_data = load_velo_scan(os.path.join(lidar_dir, x))
    lidar_data_edited = lidar_data
    lidar_data_edited[:, 0] = lidar_data_edited[:, 0] - 20  # shift the x of center axis to make object in front
    lidar_data_edited[:, 2] = lidar_data_edited[:, 2] + 1  # shift the height of center axis
    lidar_data_edited.tofile(os.path.join(save_dir, x))
