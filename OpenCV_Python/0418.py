# 영상 연산: 비트연산
import cv2
from cv2 import bitwise_and
import numpy as np

src1 = cv2.imread('./data/lena.jpg')
src2 = cv2.imread('./data/opencv_logo.png')
cv2.imshow('src2', src2)

#1 src2의 전체 크기에 대한 src1의 영역을 roi에 저장
rows, cols, channels = src2.shape
roi = src1[0:rows, 0:cols]

#2 
gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask', mask)

#3 roi 영상에서 mask의 255인 화소에서만 src1의 배경 영역을 복사
src1_bg = cv2.bitwise_and(roi, roi, mask=mask)
cv2.imshow('src1_bg', src1_bg)

#4 src2에서 전경 영역을 src2_fg에 복사
src2_fg = cv2.bitwise_and(src2, src2, mask=mask_inv)
cv2.imshow('src2_fg', src2_fg)

#5 비트 OR을 연산하여 dst를 생성
dst = cv2.bitwise_or(src1_bg, src2_fg)
cv2.imshow('dst', dst)

#6 dst를 src1에 복사하여 결과 영상 생성
src1[0:rows, 0:cols] = dst

cv2.imshow('result', src1)
cv2.waitKey()
cv2.destroyAllWindows()