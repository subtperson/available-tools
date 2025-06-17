import os 
import argparse
import xml.etree.ElementTree as ET
from tqdm import tqdm

def parse_opt():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--annotation_path', type=str, default='/media/lzy/14BA7CD7BA7CB6B8/lzy_2022/DataSets/RGBTDronePerson/train/annotation', help='folder containing xml files')
    parser.add_argument('--image_path', type=str, default='/media/lzy/14BA7CD7BA7CB6B8/lzy_2022/DataSets/RGBTDronePerson/train/thermal', help='image path, e.g. /root/LLVIP/infrared/train')
    parser.add_argument('--txt_save_path', type=str, default='/media/lzy/14BA7CD7BA7CB6B8/lzy_2022/DataSets/RGBTDronePerson/train/v5labels', help='txt path containing txt files in yolov5 format')
    opt = parser.parse_args()
    return opt
opt = parse_opt()

def convert_LLVIP_annotation(anno_path,image_path,txt_path):
    name2num = {'person':'0', 'rider':'1', 'crowd':'2', 'uncertain':'3'}

    if not os.path.exists(txt_path):
        os.makedirs(txt_path)
    for i in tqdm(os.listdir(image_path)):
        root=ET.parse(anno_path+'/'+i.split(".")[0]+'.xml').getroot()
        objects = root.findall('object')
        for obj in objects:
            annotation = ''
            bbox = obj.find('bndbox')
            xmin = int(bbox.find('xmin').text.strip())
            xmax = int(bbox.find('xmax').text.strip())
            ymin = int(bbox.find('ymin').text.strip())
            ymax = int(bbox.find('ymax').text.strip())
            x_center = str((0.5*(xmin + xmax))/640)
            y_center = str((0.5*(ymin + ymax))/512)
            width = str((xmax-xmin)/640)
            height = str((ymax-ymin)/512)
            class_name = obj.find('name').text.strip()
            annotation = annotation.join([name2num[class_name],' ',x_center,' ',y_center,' ',width,' ',height])
            with open(txt_path+'/'+i.split(".")[0]+'.txt','a') as f:
                f.write(annotation + "\n")

anno_path=opt.annotation_path
image_path=opt.image_path
txt_path=opt.txt_save_path
convert_LLVIP_annotation(anno_path,image_path,txt_path)