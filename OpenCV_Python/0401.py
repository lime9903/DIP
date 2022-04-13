# 영상 속성: 모양과 자료형
from gettext import npgettext
import cv2
import numpy as np

#img = cv2.imread('./data/lena.jpg')
img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

print('img.ndim = ', img.ndim)
print('img.shape = ', img.shape)
print('img.dtype = ', img.dtype)

img = img.astype(np.int32)
print('img.dtype = ', img.dtype)

img = np.uint8(img)
print('img.dtype = ', img.dtype)