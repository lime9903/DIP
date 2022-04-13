import cv2

imgFile = './data/lena.jpg'
img = cv2.imread(imgFile)

cv2.imwrite('./data/Lena.bmp', img)
cv2.imwrite('./data/Lena.png', img)
cv2.imwrite('./data/Lena_compression.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('./data/Lena_quality.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])