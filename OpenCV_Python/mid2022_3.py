# mid-exam 2022-3
# find the perfect matched part in the picture

import cv2
import numpy as np

src = cv2.imread('./data/manchu01.jpg')
cv2.imshow('src', src)
src_inv = cv2.bitwise_not(src)
dst = src.copy()
roi = cv2.selectROI(src_inv)
myroi = src_inv[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]
h, w = roi[3], roi[2]

result = cv2.matchTemplate(src_inv, myroi, cv2.TM_SQDIFF_NORMED)
threshold = 0.05
box_loc = np.where(result < threshold)

count = 0
for box in zip(*box_loc[::-1]):
    startX, startY = box
    endX, endY = startX + w, startY + h
    cv2.rectangle(dst, (startX, startY), (endX, endY), (255, 0, 0), 1)
    count += 1

cv2.imshow('dst', dst)
print("count= ", count)
cv2.waitKey()
cv2.destroyAllWindows()