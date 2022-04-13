# 다각형 채우기
import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
pt1 = np.array([[100, 100], [200, 100], [200, 200], [100, 200]])
pt2 = np.array([[300, 200], [400, 100], [400, 200]])

cv2.fillConvexPoly(img, pt1, color=(255, 0, 0))
cv2.fillConvexPoly(img, pt2, color=(0, 255, 0))

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()