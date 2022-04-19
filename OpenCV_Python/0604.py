# Sobel 필터 2: 에지 그래디언트 방향
import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src', src)

cv2.waitKey()
cv2.destroyAllWindows()