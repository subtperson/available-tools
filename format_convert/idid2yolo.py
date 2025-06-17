'''
用于将IDID数据集的标注转换为YOLO格式
author: lzy
date: 20240920
'''
import json
import os
import cv2
from tqdm import tqdm
from label_convert.yolo2coco import yolo2coco

json_path = "/mnt/d/Ubuntu-24.04/IDID/IDID_Train/labels_v1.2.json"
img_dir_path = "/mnt/d/Ubuntu-24.04/IDID/IDID_Train/imgs"
out_path = "/mnt/d/Ubuntu-24.04/IDID/IDID_Train/labels"



if not os.path.exists(out_path):
    os.makedirs(out_path)



json = json.load(open(json_path, 'r'))

for i in tqdm(json):
    filename = i['filename']
    img_path = os.path.join(img_dir_path, filename)
    label_save_path = os.path.join(out_path, filename.replace('.jpg', '.txt').replace('.png', '.txt')\
                                   .replace('.jpeg', '.txt').replace('.JPG', '.txt').replace('.PNG', '.txt').replace('.JPEG', '.txt'))
    # print(img_path)
    img = cv2.imread(img_path)
    h, w, _ = img.shape
    objs = i['Labels']['objects']
    with open(label_save_path, 'a') as f:
        nums = 0
        for obj in objs:
            bbox = obj['bbox']
            x_top_left = bbox[0]
            y_top_left = bbox[1]
            width = bbox[2]
            height = bbox[3]
            yolo_xcenter = x_top_left / w + width / w / 2
            yolo_ycenter = y_top_left / h + height / h / 2
            yolo_width = width / w
            yolo_height = height / h
            nums += 1

            if not obj['string']:
                if obj['conditions'].get('No issues') or obj['conditions'].get('notbroken-notflashed'):
                    cls = 0
                    # f.write(f"{cls} {yolo_xcenter} {yolo_ycenter} {yolo_width} {yolo_height}")
                    # if nums < len(objs):
                    #     f.write('\n')
                if obj['conditions'].get('glaze'):
                    cls = 1
                    f.write(f"{cls} {yolo_xcenter} {yolo_ycenter} {yolo_width} {yolo_height}")
                    if nums < len(objs):
                        f.write('\n')
                if obj['conditions'].get('shell'):
                    cls = 2
                    f.write(f"{cls} {yolo_xcenter} {yolo_ycenter} {yolo_width} {yolo_height}")
                    if nums < len(objs):
                        f.write('\n')
            else:
                cls = 0
                f.write(f"{cls} {yolo_xcenter} {yolo_ycenter} {yolo_width} {yolo_height}")
                if nums < len(objs):
                    f.write('\n')






