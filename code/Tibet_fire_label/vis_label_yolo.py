#coding=utf-8
import cv2
import os

def draw_box_in_single_image(image_path, txt_path, save_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 读取txt文件信息
    def read_list(txt_path):
        pos = []
        with open(txt_path, 'r') as file_to_read:
            while True:
                lines = file_to_read.readline()  # 整行读取数据
                if not lines:
                    break
                # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
                p_tmp = [float(i) for i in lines.split(' ')]
                pos.append(p_tmp)  # 添加新读取的数据
                # Efield.append(E_tmp)
                pass
        return pos


    # txt转换为box
    def convert(size, box):
        xmin = (box[1]-box[3]/2.)*size[1]
        xmax = (box[1]+box[3]/2.)*size[1]
        ymin = (box[2]-box[4]/2.)*size[0]
        ymax = (box[2]+box[4]/2.)*size[0]
        box = (int(xmin), int(ymin), int(xmax), int(ymax))
        return box

    pos = read_list(txt_path)
    # print(pos)
    tl = int((image.shape[0]+image.shape[1])/2)
    lf = max(tl-1,1)
    for i in range(len(pos)):
        label = str(int(pos[i][0]))
        # print('label is '+label)
        box = convert(image.shape, pos[i])
        image = cv2.rectangle(image,(box[0], box[1]),(box[2],box[3]),(0,255,0),5)
        cv2.putText(image,label,(box[0],box[1]-2), 0, 1, [0,255,0], thickness=2, lineType=cv2.LINE_AA)
        pass

    if pos:
        cv2.imwrite(save_path, image)
    else:
        print('None')





img_folder = "C:\\Users\\lance\\Desktop\\new_fire\\GT"
img_list = os.listdir(img_folder)
img_list.sort()

label_folder = "C:\\Users\\lance\\Desktop\\firetest\\l"
label_list = os.listdir(label_folder)
label_list.sort()

save_folder = "C:\\Users\\lance\\Desktop\\firetest\\save"

for i in range(len(img_list)):
    image_path = img_folder + "\\" + img_list[i]
    txt_path = label_folder + "\\" + label_list[i]
    save_path = save_folder + "\\" + img_list[i]
    draw_box_in_single_image(image_path, txt_path, save_path)
    print("finish %d" % i)

