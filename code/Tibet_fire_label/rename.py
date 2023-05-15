# coding=utf-8



import os
import shutil

# os获取工作目录
os.chdir('C:\\Users\\lance\\Desktop\\new_fire\\RGB')
list = os.listdir()
list.sort()

# 重命名
for i in range(len(list)):
    os.rename(list[i],  str(i).zfill(3) + '.png')













