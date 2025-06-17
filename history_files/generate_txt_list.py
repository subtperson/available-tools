'''
生成txt文件列表
author: lzy
date: 20240924
'''

import os

train_txt_dir = '/mnt/d/Ubuntu-24.04/IDID/myidid/train/labels'
val_txt_dir = '/mnt/d/Ubuntu-24.04/IDID/myidid/val/labels'

train_txt_list = os.listdir(train_txt_dir)
val_txt_list = os.listdir(val_txt_dir)

with open('/mnt/d/Ubuntu-24.04/IDID/myidid/train.txt', 'w') as f:
    for txt in train_txt_list:
        f.write(f"/mnt/d/Ubuntu-24.04/IDID/myidid/train/imgs/{txt.replace('.txt', '.jpg')}\n")

with open('/mnt/d/Ubuntu-24.04/IDID/myidid/val.txt', 'w') as f:
    for txt in val_txt_list:
        f.write(f"/mnt/d/Ubuntu-24.04/IDID/myidid/val/imgs/{txt.replace('.txt', '.jpg')}\n")    
