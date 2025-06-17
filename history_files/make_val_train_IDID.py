'''
用于将IDID数据集划分为训练集和验证集，考虑经过增强之后重复图片问题，更严谨
author: lzy
date: 20240924
'''

import os
import random
from tqdm import tqdm




img_dir = "/mnt/d/Ubuntu-24.04/IDID/IDID_Train/imgs"
labels_dir = "/mnt/d/Ubuntu-24.04/IDID/IDID_Train/labels"
val_img_dir = '/mnt/d/Ubuntu-24.04/IDID/myidid/val/imgs'
val_labels_dir = '/mnt/d/Ubuntu-24.04/IDID/myidid/val/labels'
train_img_dir = '/mnt/d/Ubuntu-24.04/IDID/myidid/train/imgs'
train_labels_dir = '/mnt/d/Ubuntu-24.04/IDID/myidid/train/labels'
os.makedirs(val_img_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)
os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)

img_list = os.listdir(img_dir)
new_img_list = []

for img in img_list:
    img1 = img.split('.')[0].replace('v', '').replace('d', '').replace('h', '')
    new_img_list.append(img1)

img_list_no_overlap = list(set(new_img_list))

# print(len(img_list_no_overlap))

# # random split
train_img_list = random.sample(img_list_no_overlap, int(len(img_list_no_overlap) * 0.75))
val_img_list = list(set(img_list_no_overlap) - set(train_img_list))

# 人工筛选
val_img_list = ['161030', '160693', '1506212', '170235', '100279', '161211', '130027', '160164', '150476', '1701602', 
       '150707', '150500', '160716', '170166', '160842', '161396', '160190', '160435', '161410', '130015', 
       '160778', '1506022', '170484', '15072', '130119', '161439', '151191', '160896', '161409', '160730', 
       '170046', '1705022', '16064', '170174', '161020', '161219', '1705132', '170806', '160096', '150951', 
       '170031', '1705062', '161177', '161423', '160840', '110008', '170685', '170059', '170522', '150347', 
       '1507142', '160442', '150760', '170103', '100228', '130019', '150907', '170208', '150460', '1703172', 
       '161099', '150864', '1600822', '150473', '170088', '130031', '161502', '150631', '161516', '170173', 
       '130113', '100017', '140021', '161057', '1702112', '170160', '150677', '150915', '150800', '170087', 
       '1708232', '110009', '150633', '170708', '170030', '161338', '161276', '170810', '150950', '161397', 
       '170527', '170526', '150346', '160643', '170037', '170148', '170569', '170615', '1505992', '1506642']
train_img_list = list(set(img_list_no_overlap) - set(val_img_list))


print(train_img_list)
print(val_img_list)
print('yes' if '160454' in train_img_list else 'no')



for img in tqdm(img_list):
    img1 = img.split('.')[0].replace('v', '').replace('d', '').replace('h', '')
    if img1 in train_img_list:
        os.system(f"cp {os.path.join(img_dir, img)} /mnt/d/Ubuntu-24.04/IDID/myidid/train/imgs")
        os.system(f"cp {os.path.join(labels_dir, img.replace('.jpg', '.txt'))} /mnt/d/Ubuntu-24.04/IDID/myidid/train/labels")
        
    if img1 in val_img_list:
        os.system(f"cp {os.path.join(img_dir, img)} /mnt/d/Ubuntu-24.04/IDID/myidid/val/imgs")
        os.system(f"cp {os.path.join(labels_dir, img.replace('.jpg', '.txt'))} /mnt/d/Ubuntu-24.04/IDID/myidid/val/labels")
        
