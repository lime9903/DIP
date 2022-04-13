# 2차원 균등분포 난수 좌표
import cv2
import numpy as np
import time

dst = np.full((512,512,3), (255,255,255), dtype=np.uint8)
nPoints = 100
pts = np.zeros((1, nPoints, 2), dtype=np.uint16)

# generate random number
cv2.setRNGSeed(int(time.time()))
cv2.randu(pts, (0, 0), (512, 512))

# draw points
for k in range(nPoints):
    x, y = pts[0, k][:]
    cv2.circle(dst, (x, y), radius=5, color=(0,0,255), thickness=-1)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()