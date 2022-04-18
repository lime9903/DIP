# mid-exam 2022 prepare
# find the perfect matched part in the picture

import cv2
import numpy as np

src = cv2.imread('./data/manchu01.jpg')
dst = src.copy()
roi = cv2.selectROI(src)
myroi = src[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]
h, w = roi[3], roi[2]

result = cv2.matchTemplate(src, myroi, cv2.TM_SQDIFF_NORMED)
threshold = 0.08
box_loc = np.where(result < threshold)

for box in zip(*box_loc[::-1]):
    startX, startY = box
    endX, endY = startX + w, startY + h
    cv2.rectangle(dst, (startX, startY), (endX, endY), (255, 0, 0), 1)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()