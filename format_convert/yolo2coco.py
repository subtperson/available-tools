'''
用于将YOLO格式的标注转换为COCO格式
author: lzy
date: 20241114
'''

import os
import json
import cv2
from tqdm import tqdm

def yolo2coco(yolo_path, img_dir, out_path):
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    
    img_list = os.listdir(img_dir)
    img_list = [i for i in img_list if i.endswith('.jpg') or i.endswith('.png') or i.endswith('.jpeg')]
    
    data = {}
    data['images'] = []
    data['annotations'] = []
    data['categories'] = [{'id': 0, 'name': 'string'}, {'id': 1, 'name': 'flashed'}, {'id': 2, 'name': 'broken'}]
    
    img_id = 0
    ann_id = 0
    for img_name in tqdm(img_list):
        img_id += 1
        img_path = os.path.join(img_dir, img_name)
        img = cv2.imread(img_path)
        h, w, _ = img.shape
        
        img_info = {'file_name': img_name, 'height': h, 'width': w, 'id': img_id}
        data['images'].append(img_info)
        
        label_path = os.path.join(yolo_path, img_name.replace('.jpg', '.txt'))
        # print(label_path)
        with open(label_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                ann_id += 1
                line = line.strip().split(' ')
                cls = int(line[0])
                xcenter = float(line[1])
                ycenter = float(line[2])
                width = float(line[3])
                height = float(line[4])
                
                x_top_left = int((xcenter - width / 2) * w)
                y_top_left = int((ycenter - height / 2) * h)
                width = int(width * w)
                height = int(height * h)
                
                ann = {'image_id': img_id, 'bbox': [x_top_left, y_top_left, width, height], 'category_id': cls, 'id': ann_id, 'iscrowd': 0}
                data['annotations'].append(ann)

    with open(os.path.join(out_path, 'val.json'), 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    yolo_path = "/mnt/d/Ubuntu-24.04/IDID/myidid/val/labels"
    img_dir = "/mnt/d/Ubuntu-24.04/IDID/myidid/val/imgs"
    out_path = "/mnt/d/Ubuntu-24.04/IDID/myidid"
    yolo2coco(yolo_path, img_dir, out_path)