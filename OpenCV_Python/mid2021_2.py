# 2021 mid exam - (2)

import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg')  # cv2.IMREAD_COLOR
dst = src.copy()
roi = cv2.selectROI(src)
print('roi=', roi)

dst[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2], 2] = 255

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()