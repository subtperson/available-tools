#coding=utf-8
import os

import cv2
import numpy as np


def get_label(image_path, save_label_path):
    print(image_path, save_label_path)
    img = cv2.imread(image_path)
    img_w = img.shape[1]
    img_h = img.shape[0]
    print(img.shape, img_w, img_h)

    r_channel = img[:, :, 0]
    r_channel =255 - r_channel
    a, b = np.nonzero(r_channel)

    print(a)
    print(b)
    xmin = min(b)
    xmax = max(b)
    ymin = min(a)
    ymax = max(a)
    xcenter = (xmin + xmax) / 2
    ycenter = (ymin + ymax) / 2
    xwidth = xmax - xmin
    yheight = ymax - ymin

    boxs = []
    temp = [0, 0, 0, 0, 0]
    temp.append(xcenter)
    temp[1] = xcenter / img_w
    temp[2] = ycenter / img_h
    temp[3] = xwidth / img_w
    temp[4] = yheight / img_h
    boxs.append(temp)   # 最后剩下的有用的框

    f = open(save_label_path, "w+")
    for line in boxs:
        line = str(line)[1:-2].replace(",","")
        print(line)
        f.write(line+"\n")
    f.close()


if __name__ == '__main__':
    img_floder = "C:\\Users\\lance\\Desktop\\new_fire\\GT-459-471"
    save_label_floder = "C:\\Users\\lance\\Desktop\\firetest\\l-459-471"
    for i in range(459, 472):
        img_path = img_floder + "\\" + str(i).zfill(3) + ".png"
        save_label_path = save_label_floder + "\\" + str(i).zfill(3) + ".txt"
        get_label(img_path, save_label_path)
        print("finish %d" % i)


