import cv2
import numpy as np

video = cv2.VideoCapture(0)

while(True):
    _, frame = video.read()
    pixel=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    altmavi=np.array([110,50,50])
    ustmavi=np.array([130,255,255])

    mask=cv2.inRange(pixel, altmavi, ustmavi)
    a=cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('hi', mask)

    key=cv2.waitKey(5) & 0xFF

    if key==27:
        break


cv2.destroyAllWindows()
