# 화소 접근: 컬러 영상 (BGR)
import cv2
import numpy as np

img = cv2.imread('./data/lena.jpg')   # cv2.IMREAD_COLOR
img[100, 200] = [255, 0, 0]   # 화소값 [100, 200]의 값을 Blue로
print(img[100:110, 200:210])

img[100:400, 200:300] = [0, 255, 255]   # ROI 접근

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()