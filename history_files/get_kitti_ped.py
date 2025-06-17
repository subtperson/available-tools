#coding=utf-8
# 获取kitti数据集中含有行人的数据

import os
import numpy as np


train_list = []
train = open('C:\\Users\\lance\\Desktop\\train.txt', 'r')
for line in train.readlines():
    train_list.append(line.strip('\n'))
train.close()

val_list = []
val = open('C:\\Users\\lance\\Desktop\\val.txt', 'r')
for line in val.readlines():
    val_list.append(line.strip('\n'))
val.close()




label_path = "C:\\Users\\lance\\Desktop\\label_2"
save_path = "C:\\Users\\lance\\Desktop\\label_2_ped"
txt_list = os.listdir(label_path)
txt_list.sort()
print(txt_list)
print(len(txt_list))
txt_list.remove('desktop.ini')
count = 0
for i in range(len(txt_list)):
    file_path = label_path + '\\' + txt_list[i]
    with open(file_path, 'r') as f:
        lines = f.readlines()
        # for line in lines:
        #     if not line.split(' ')[0] == 'Pedestrian':
        #     # delete this row
        #         line.replace(line, '')
        #         print(txt_list[i])
        #         count = count + 1
        #         break


        for line in lines:
            if line.split(' ')[0] == 'Pedestrian' and val_list.__contains__(txt_list[i].split('.')[0]):
                print(txt_list[i].split('.')[0])
                count = count + 1
                # with open(save_path + '\\' + txt_list[i], 'w') as ff:
                #     ff.writelines(lines)
                #     ff.close()
                break


print('count is ' + str(count))
# print(len(train_list))


