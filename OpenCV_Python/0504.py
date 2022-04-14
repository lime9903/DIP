# 히스토그램 계산 2: 그레이스케일 영상
import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

hist1 = cv2.calcHist(images=[src], channels=[0], mask=None,
                     histSize=[32], ranges=[0,256])

hist2 = cv2.calcHist(images=[src], channels=[0], mask=None,
                     histSize=[256], ranges=[0,256])

#1 1차원 행 배열로 변경
hist1 = hist1.flatten()
hist2 = hist2.flatten()

#2 hist1 그리기
plt.title('hist1: binX = np.arange(32)')
plt.plot(hist1, color='r')
binX = np.arange(32)
plt.bar(binX, hist1, width=1, color='b')
plt.show()

#3 hist1 - arange(32)*8 그리기
plt.title('hist1: binX = np.arange(32)*8')
binX = np.arange(32)*8
plt.plot(binX, hist1, color='r')
plt.bar(binX, hist1, width=8, color='b')
plt.show()

#4 hist2 그리기
plt.title('hist2: binX = np.arange(256)')
binX = np.arange(256)
plt.plot(binX, hist2, color='r')
plt.bar(binX, hist2, width=1, color='b')
plt.show()