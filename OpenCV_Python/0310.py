# 키보드 이벤트 처리
import cv2
import numpy as np

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

width, height = 512, 512
x, y, R = 256, 256, 50
direction = 0

while True:
    key = cv2.waitKeyEx(30)
    if key == 0x1B:   # ESC
        break

# 방향키 방향 전환
    elif key == 0x270000: # right key
        direction = RIGHT
    elif key == 0x280000: # down key
        direction = DOWN
    elif key == 0x250000: # left key
        direction = LEFT
    elif key == 0x260000: # up key
        direction = UP

# 방향으로 이동
    if direction == RIGHT:
        x += 10
    elif direction == DOWN:
        y += 10
    elif direction == LEFT:
        x -= 10
    elif direction == UP:
        y -= 10
        
# 경계 확인
    if x < R:
        x = R
        direction = RIGHT
    if x > width - R:
        x = width - R
        direction =LEFT
    if y < R:
        y = R
        direction = DOWN
    if y > height - R:
        y = height - R
        direction = UP
        
# 지우고, 그리기
    img = np.zeros((width, height, 3), np.uint8) + 255
    cv2.circle(img, (x, y), R, (0, 0, 255), -1)
    cv2.imshow('img', img)
cv2.destroyAllWindows()