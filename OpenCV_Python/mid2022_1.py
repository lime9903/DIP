# 2022 mid exam - 1
# move the circle + random color

import cv2
import numpy as np

width, height = 512, 512
x, y, R = 256, 256, 50
direction = 0
r, g, b = 255, 0, 0
r_, g_, b_ = 0, 0, 0

while True:
    key = cv2.waitKeyEx(30)
    if key == 0x1B:
        break
    
    # 방향키 방향 전환
    elif key == 0x270000:  # right
        direction = 0
    elif key == 0x280000:  # down
        direction = 1
    elif key == 0x250000:  # left
        direction = 2
    elif key == 0x260000:  # up
        direction = 3
    elif key == 0x700000:
        r = np.random.randint(256)
        g = np.random.randint(256)
        b = np.random.randint(256)
        r_ = np.random.randint(256)
        g_ = np.random.randint(256)
        b_ = np.random.randint(256)

    
    # 방향으로 이동
    if direction == 0:
        x += 10
    elif direction == 1:
        y += 10
    elif direction == 2:
        x -= 10
    else:
        y -= 10
        
    # 경계 확인
    if x <= -R:        # if the circle meets the left end
        x = width + R
        direction = 2
    if x > width + R:  # if the circle meets the right end     
        x = -R
        direction = 0
    if y < -R:         # if the circle meets the upper end
        y = height + R
        direction = 3
    if y > height + R: # if the circle meets the bottom end 
        y = -R
        direction = 1

    # 지우고, 그리기
    img = np.zeros((width, height, 3), np.uint8) + 255
    cv2.circle(img, (x, y), R, (r, g, b), -1)
    cv2.circle(img, (x, y), R, (r_, g_, b_), 2)
    cv2.imshow('img', img)

cv2.destroyAllWindows()