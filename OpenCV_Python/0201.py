# read and print
import cv2

imgFile = './data/lena.jpg'
img = cv2.imread(imgFile)
greyimg = cv2.imread(imgFile, cv2.IMREAD_GRAYSCALE)

cv2.imshow('Lena color', img)
cv2.imshow('Lena grey scale', greyimg)

cv2.waitKey()
cv2.destroyAllWindows()