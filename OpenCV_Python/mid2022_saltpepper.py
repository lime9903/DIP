# mid-exam 2022 prepare
# generate salt and pepper

import cv2
import numpy as np
import time

src = cv2.imread('./data/lena.jpg')
dst = src.copy()
cv2.imshow('src', src)

height, width = src.shape[0], src.shape[1]
N = int(((height*width) * (0.5/100)) / 4)
pts = np.zeros((1, N, 2), dtype = np.uint16)
cv2.setRNGSeed(int(time.time()))
cv2.randu(pts, (0, 0), (512, 512))

# draw points
for k in range(N):
    x, y = pts[0, k][:]
    cv2.circle(dst, (x, y), radius=1, color=(0, 0, 0), thickness=-1)
# if you want to generate a salt error,
# just change the parameter 'color=(255, 255, 255)'

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()