# ROI 부분만 equalization
import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg')
dst = src.copy()
roi = cv2.selectROI(src)

#1
my_roi = src[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]
hsv = cv2.cvtColor(my_roi, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

v2 = cv2.equalizeHist(v)
hsv2 = cv2.merge([h, s, v2])
dst[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]] = cv2.cvtColor(hsv2, cv2.COLOR_HSV2BGR)
cv2.imshow('dst', dst)

cv2.waitKey()    
cv2.destroyAllWindows()