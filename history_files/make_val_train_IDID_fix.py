'''
用于将IDID数据集划分为训练集和验证集，不考虑经过增强之后重复图片，不严谨版本
author: lzy
date: 20241028
'''

import os
import random

img_dir = "/mnt/d/Ubuntu-24.04/InsulatorDet/IDID_Train/imgs"
labels_dir = "/mnt/d/Ubuntu-24.04/InsulatorDet/IDID_Train/labels"
new_imgs_dir = "/mnt/d/Ubuntu-24.04/InsulatorDet/IDID_Train/new-imgs"
img_list = os.listdir(img_dir)
new_img_list = []

# for img in img_list:
#     img1 = img.split('.')[0].replace('v', '').replace('d', '').replace('h', '')
#     new_img_list.append(img1)

# img_list_no_overlap = list(set(new_img_list))

# print(len(img_list_no_overlap))

# random split
train_img_list = random.sample(img_list, int(len(img_list) * 0.75))
val_img_list = list(set(img_list) - set(train_img_list))

print(len(val_img_list))

for img in img_list:
    # img1 = img.split('.')[0].replace('v', '').replace('d', '').replace('h', '')
    if img in train_img_list:
        os.system(f"cp {os.path.join(img_dir, img)} /mnt/d/Ubuntu-24.04/InsulatorDet/myidid/train/imgs")
        os.system(f"cp {os.path.join(labels_dir, img.replace('.jpg', '.txt'))} /mnt/d/Ubuntu-24.04/InsulatorDet/myidid/train/labels")
        
    if img in val_img_list:
        os.system(f"cp {os.path.join(img_dir, img)} /mnt/d/Ubuntu-24.04/InsulatorDet/myidid/val/imgs")
        os.system(f"cp {os.path.join(labels_dir, img.replace('.jpg', '.txt'))} /mnt/d/Ubuntu-24.04/InsulatorDet/myidid/val/labels")
        
