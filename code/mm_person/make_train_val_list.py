import numpy
import torch
import os



path = '/media/vision/lzy/data/RGBTDronePerson/visible/test'

file_list = os.listdir(path)
file_list.sort()

# save csv
save_path = '/media/vision/lzy/data/RGBTDronePerson/visible/test.csv'
numpy.savetxt(save_path, file_list, delimiter=',', fmt='%s')

# x0 = torch.load("/media/vision/lzy/mm_person/multispectral-object-detection/lzy_tools/x0.pt")
# score = torch.load("/media/vision/lzy/mm_person/multispectral-object-detection/lzy_tools/fus_score.pt")
# print(x0.shape)
# print(score.shape)
# print(x0)
# print(score)

# score = [2,4]

# x0[0] = x0[0].clone()*2
# print(re)


# a = torch.tensor([
#     [[1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10]],
#     [[1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10]]
#     ])
# b = torch.tensor([2,3])
# b = b.unsqueeze(-1).unsqueeze(-1)
# print(a)
# # print(b)
# print(a.shape)
# print(b.shape)

# c = a*b
# print(c)

# a[0] = a[0]*10

# print(a)




# ir = '/media/vision/lzy/mm_person/multispectral-object-detection/datasets/LLVIP/infrared/train'
# rgb = '/media/vision/lzy/mm_person/multispectral-object-detection/datasets/LLVIP/visible/train'

# irlist = os.listdir(ir)
# rgblist = os.listdir(rgb)
# # count=0
# # for i in irlist:
# #     if i in rgblist:
# #         print(i)
# #         count+=1
# #         # os.remove(os.path.join(ir, i))
# #         # os.remove(os.path.join(ir, i[:-4]+'.txt'))
# #         # os.remove(os.path.join(ir, i[:-4]+'.xml'))
# # print(count)

# label = '/media/vision/lzy/mm_person/multispectral-object-detection/datasets/LLVIP/labels/train'
# label_list = os.listdir(label)
# print(len(label_list))

# for i in irlist:
#     if i[:-4]+'.txt' not in label_list:
#         print(i)
#         # os.remove(os.path.join(ir, i))
#         # os.remove(os.path.join(ir, i[:-4]+'.txt'))
#         # os.remove(os.path.join(ir, i[:-4]+'.xml'))