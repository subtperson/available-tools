import os
import numpy as np
import sys

label_dir = 'C:\\Users\\lance\\Desktop\\subtperson\\edgar\\training\\label'
save_dir = 'C:\\Users\\lance\\Desktop\\subtperson\\edgar\\training\\label_edited'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)



for x in os.listdir(label_dir):
    with open(os.path.join(label_dir, x), 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(' ')
            line[13] = str(round(float(line[13]) - 20, 2))
            line[12] = str(round(float(line[12]) - 1, 2))
            line = ' '.join(line)
            print(x+line)
            with open(os.path.join(save_dir, x), 'a') as f2:
                f2.write(line)

