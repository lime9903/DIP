# 화소 접근: 그레이스케일 영상
import cv2
import numpy as np

img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
img[100, 200] = 0                # 화소값 (밝기, 그레이스케일) 변경
print(img[100:110, 200:210])     # ROI 접근

img[100:400, 200:300] = 0

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()