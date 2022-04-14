# 적응형 임계값 영상
import cv2
import numpy as np

src = cv2.imread('./data/srcThreshold.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src', src)

ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print('Binary + Otsu ret = ', ret)
cv2.imshow('Threshold: Binary + Otsu', dst)

dst2 = cv2.adaptiveThreshold(src, 255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 51, 7)
cv2.imshow('Adaptive threshold: Gaussian + Binary', dst2)

dst3 = cv2.adaptiveThreshold(src, 255,
                                   cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY, 51, 7)
cv2.imshow('Adaptive threshold: Binary + Mean', dst3)

cv2.waitKey()
cv2.destroyAllWindows()