import os

import numpy

path = 'D:\\#FFF\\rgbt\\TJ662\\labels'

file_list = os.listdir(path)

# save csv
save_path = 'D:\\#FFF\\rgbt\\TJ662\\labels.csv'
numpy.savetxt(save_path, file_list, delimiter=',', fmt='%s')