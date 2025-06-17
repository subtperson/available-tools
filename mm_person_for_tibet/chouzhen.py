import os

import numpy
import cv2

video_dir = '/media/lzy/14BA7CD7BA7CB6B8/lzy_2022/mm_person/rgbt26'
video_name = '08-1.mp4'
video_path = video_dir + '/' + video_name
save_path = video_path.replace('.mp4', '')
if not os.path.exists(save_path):
    os.makedirs(save_path)


vc = cv2.VideoCapture(video_path)  # 读入视频文件
rval, frame = vc.read()

fps = vc.get(cv2.CAP_PROP_FPS)
frame_all = vc.get(cv2.CAP_PROP_FRAME_COUNT)
print(fps)
print(frame_all)

frame_interval = 1

frame_count = 0

while rval:  # 循环读取视频帧
    rval, frame = vc.read()
    if frame_count % frame_interval == 0:
        cv2.imwrite(save_path + '/' + str(frame_count) + '.jpg', frame)  # 存储为图像
    frame_count = frame_count + 1
    cv2.waitKey(1)
    if frame_count > 30*10:
        break




