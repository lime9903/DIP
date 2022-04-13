# 여백 조정 및 영상 저장
import cv2
import matplotlib.pyplot as plt

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=(6,6))
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.savefig('./data/0205lena.png')
plt.show()