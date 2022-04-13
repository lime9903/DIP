# 화소 접근: 컬러 영상 (채널 접근)
import cv2
import numpy as np

img = cv2.imread('./data/lena.jpg')

img[100:400, 200:300, 0] = 255  # Channel-B
img[100:400, 300:400, 1] = 255  # Channel-G
img[100:400, 400:500, 2] = 255  # Channel-R

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()