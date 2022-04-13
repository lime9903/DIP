# video capture and display
import cv2

#cap = cv2.VideoCapture(0)  # 연결된 카메라가 있을 때
cap = cv2.VideoCapture('./data/vtest.avi')
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
             int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame size = ', frame_size)

while True:
    retval, frame = cap.read()
    if not retval:  # 영상이 끝난 경우
        break
    
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(25)  # 25/1000 delay
    if key == 27:  # ESC: escape
        break
    
if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()