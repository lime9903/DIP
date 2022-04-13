import cv2
import matplotlib.pyplot as plt

imgFile = './data/lena.jpg'
imgBGR = cv2.imread(imgFile)

imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
plt.imshow(imgRGB)
plt.axis('off')
plt.show()