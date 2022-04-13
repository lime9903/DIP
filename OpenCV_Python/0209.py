# youtube 동영상
import cv2
import pafy

url = 'https://youtu.be/lX44CAz-JhU'
video = pafy.new(url)

print("title = {}".format(video.title))
print("video rating = {}".format(video.rating))
print("video duration = {}".format(video.duration))

best = video.getbest()
print("best resolution = {}".format(best.resolution))

cap = cv2.VideoCapture(best.url)

while(True):
    retval, frame = cap.read()
    
    if not retval:
        break
    cv2.imshow('frame', frame)
    
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grey, 100, 200)
    cv2.imshow('edges', edges)
    
    key = cv2.waitKey(25)
    if key == 27:
        break

cv2.destroyAllWindows()