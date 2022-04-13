# matplotlib 비디오 디스플레이
import cv2
import matplotlib.pyplot as plt

def handle_key_press(event):
    if event.key == 'escape':
        cap.release()
        plt.close()

def handle_close(event):
    print("Close figure!")
    cap.release()
    
# 프로그램 시작
cap = cv2.VideoCapture('./data/vtest.avi')

plt.ion() # 대화 모드 설정
fig = plt.figure(figsize=(10, 6))
plt.axis('off')

fig.canvas.manager.set_window_title('Video Capture')
fig.canvas.mpl_connect('key_press_event', handle_key_press)
fig.canvas.mpl_connect('close_event', handle_close)

retval, frame = cap.read()
im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

# 3
while True:
    retval, frame = cap.read()
    if not retval:
        break
    
    im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    fig.canvas.draw()
    fig.canvas.flush_events()
    
if cap.isOpened:
    cap.release