import cv2

img1_path = '/media/zxu/bfde2656-931a-4533-b284-9b2db755a2ee/lzy22/getdata/ok_data/rgb/a0001.jpg'
img1 = cv2.imread(img1_path)
img2_path = img1_path.replace('rgb', 'ir')
img2 = cv2.imread(img2_path)
print(img1.shape, img2.shape)
img1 = cv2.resize(img1, (860, 480))

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
cv2.imshow('img', img3, )
cv2.waitKey(0)



