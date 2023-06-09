#coding=utf-8
# 统计数据集标注的高度

import os

import numpy as np

path = 'C:\\Users\\lance\\Desktop\\subtperson\\edgar\\training\\label'
label_list = os.listdir(path)
label_list = label_list[700:999] # 只统计验证集

print(label_list)

height_list = []

for label_file in label_list:
    label_path = path + '\\' + label_file
    with open(label_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            height_list.append(float(line.split(' ')[8]))

print(height_list)

# save list to csv file
np.savetxt('C:\\Users\\lance\\Desktop\\subtperson\\edgar\\training\\val_height.csv', height_list, delimiter=',', fmt='%.2f')












