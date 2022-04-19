# mid 2022-2
# mosaic ROI area 

import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg')  # cv2.IMREAD_COLOR
dst = src.copy()
roi = cv2.selectROI(src)

N = 16  # 4, 8, 16, 32, 64, ...
height, width = roi[3], roi[2]
h = height // N
w = width // N
for i in range(N):
    for j in range(N):
        y = i * h + roi[1]
        x = j * w + roi[0]
        mini_roi = src[y:y+h, x:x+w]
        dst[y:y+h, x:x+w] = cv2.mean(mini_roi)[0:3]

cv2.imshow('dst', dst)

print('s_y=', roi[1])
print('s_x=', roi[0])
print('d_y=', roi[3])
print('d_x=', roi[2])

cv2.waitKey()
cv2.destroyAllWindows()