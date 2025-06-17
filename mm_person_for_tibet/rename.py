import os

import numpy
import cv2

video_dir = '/media/zxu/bfde2656-931a-4533-b284-9b2db755a2ee/lzy22/getdata/rgbt/20230711new/20230711/192.168.54.203_8000_1_4BFB783B54FC46A6A80BB1984DE7FEDD_'
video_name = 'b2-ir.mp4'
video_path = video_dir + '/' + video_name
save_path = video_path.replace('.mp4', '')
if not os.path.exists(save_path):
    os.makedirs(save_path)

# save_path = '/media/zxu/bfde2656-931a-4533-b284-9b2db755a2ee/lzy22/getdata/image'
list = os.listdir(save_path)
list.sort(key=lambda x: int(x[:-4]))
print(list)
for i in range(0, len(list)):
    path = os.path.join(save_path, list[i])
    print(path)
    os.rename(path, os.path.join(save_path, 'b' + str(i).zfill(4) + '.jpg'))

