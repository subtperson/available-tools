import numpy as np
import os

# path = '/media/lzy/14BA7CD7BA7CB6B8/lzy_2022/subt_person/ST3D/data/edgar/gt_database/'
# label_list = os.listdir(path)
# print(label_list)

# all_pc = []
# for pc in label_list:
#     pc_path = path + pc
#     pc_data = np.fromfile(pc_path, dtype=np.float32).reshape(-1, 4)
#     # print(pc_data.shape)
#     all_pc.append(pc_data)
# print(len(all_pc))
# all_pc = np.concatenate(all_pc, axis=0)
# print(all_pc.shape)
# print(all_pc.shape[0]/3533)

a = np.array([[1,8],[3,4],[5,6]])
re = np.where(a[:,1]>2)
print(re)





