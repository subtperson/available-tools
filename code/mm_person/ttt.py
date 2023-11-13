import os

import cv2
import numpy as np


class AffineTransformer:
    def __init__(self):
        self.source_points = []
        self.target_points = []
        self.transformation_matrix = None

    def set_points(self, source_points, target_points):
        self.source_points = np.float32(source_points)
        self.target_points = np.float32(target_points)

    def calculate_transformation_matrix(self):
        self.transformation_matrix = cv2.getAffineTransform(self.source_points, self.target_points)

    def apply_transform(self, image):
        if self.transformation_matrix is None:
            raise ValueError("Transformation matrix has not been calculated.")
        else:
            rows, cols = image.shape[:2]
            return cv2.warpAffine(image, self.transformation_matrix, (1920, 1080))


transformer = AffineTransformer()  # 创建仿射变换器实例

img_dir = '/media/lzy/14BA7CD7BA7CB6B8/lzy_2022/mm_person/rgbt26/ir'
save_dir = img_dir.replace('ir_ori', 'ir_trans')
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

source_points = [[368, 142], [89, 121], [506, 456]]
target_points = [[1002, 413], [611, 381], [1204, 855]]

transformer.set_points(source_points, target_points)
# 计算仿射变换矩阵
transformer.calculate_transformation_matrix()

img_list = os.listdir(img_dir)
img_list.sort()
print(img_list)

for img_name in img_list:
    img_path = os.path.join(img_dir, img_name)
    save_path = os.path.join(save_dir, img_name)
    # 读取原始图像
    image = cv2.imread(img_path)
    # 应用仿射变换
    transformed_image = transformer.apply_transform(image)
    cv2.imwrite(save_path, transformed_image)
    print('finish %s' % img_name)

# # 读取原始图像
# image = cv2.imread(img_path)
# # 应用仿射变换
# transformed_image = transformer.apply_transform(image)
# cv2.imwrite('C:\\Users\\lance\\Desktop\\WechatIMG855_T2.jpg', transformed_image)

# b3
# source_points = [[575, 329], [513, 96], [39, 275]]
# target_points = [[2132, 963], [1940, 240], [463, 791]]

# b1
# source_points = [[132, 212], [604, 284], [293, 493]]
# target_points = [[773, 613], [2111, 820], [1230, 1401]]

# h1
# source_points = [[809, 336], [420, 370], [803, 283]]
# target_points = [[1499, 671], [1009, 721], [1492, 582]]

# h2
# source_points = [[181, 65], [392, 251], [567, 270]]
# target_points = [[624, 117], [949, 505], [1226, 551]]