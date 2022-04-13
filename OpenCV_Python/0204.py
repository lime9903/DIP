# grey scale image show=
import cv2
import matplotlib.pyplot as plt
imgFile = './data/lena.jpg'
img = cv2.imread(imgFile, cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()