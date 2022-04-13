# 직선 및 사각형 그리기
import cv2
import numpy as np

# white 배경 생성
img = np.zeros(shape = (512, 512, 3), dtype = np.uint8) + 255
# img = np.ones(shape = (512, 512, 3), np.unit8) * 255

pt1 = 100, 100
pt2 = 400, 400
cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)

start = 0, 0
end = 500, 0
cv2.line(img, start, end, (255, 0, 0), 5)
cv2.line(img, (0, 0), (0, 500), (0, 0, 255), 5)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()