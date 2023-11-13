# Function: cut the image edge
import os

import cv2

ir_dir = 'D:\\#FFF\\rgbt\\ok_data\\ir_trans\\h1'
ir_save_dir = ir_dir.replace('ir_trans', 'ir')
rgb_dir = ir_dir.replace('ir_trans', 'rgb_ori')
rgb_save_dir = ir_save_dir.replace('ir', 'rgb')
if not os.path.exists(ir_save_dir):
    os.mkdir(ir_save_dir)
if not os.path.exists(rgb_save_dir):
    os.mkdir(rgb_save_dir)

img_list = os.listdir(ir_dir)
img_list.sort()
print(img_list)

for img_name in img_list:
    ir_path = os.path.join(ir_dir, img_name)
    ir_save_path = os.path.join(ir_save_dir, img_name)
    rgb_path = os.path.join(rgb_dir, img_name)
    rgb_save_path = os.path.join(rgb_save_dir, img_name)
    # cut the image edge
    ir_img = cv2.imread(ir_path)
    ir_img = ir_img[180:1080-120, 550:1920-330]
    ir_img = cv2.resize(ir_img, (1600, 1200))
    cv2.imwrite(ir_save_path, ir_img)
    rgb_img = cv2.imread(rgb_path)
    rgb_img = rgb_img[180:1080-120, 550:1920-330]
    rgb_img = cv2.resize(rgb_img, (1600, 1200))
    cv2.imwrite(rgb_save_path, rgb_img)
    print('finish %s' % img_name)


'''
1200*1600
'''