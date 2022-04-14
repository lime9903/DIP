# mid 2022 prepare
# cut logo and paste to src

import cv2
import numpy as np

src1 = cv2.imread('./data/lena.jpg')
src2 = cv2.imread('./data/opencv_logo.png')

height, width = src1.shape[0], src1.shape[1]
rows, cols, channels = src2.shape
roi = src1[height-rows:height, width-cols:width]

gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

src1_bg = cv2.bitwise_and(roi, roi, mask=mask)
src2_fg = cv2.bitwise_and(src2, src2, mask=mask_inv)
dst = cv2.bitwise_or(src1_bg, src2_fg)
src1[height-rows:height, width-cols:width] = dst

cv2.imshow('result', src1)
cv2.waitKey()
cv2.destroyAllWindows()