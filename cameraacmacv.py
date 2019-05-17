import cv2
import numpy as np

video=cv2.VideoCapture(0)

while(True):
    ret,frame=video.read()
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Ojen',gri)

    if cv2.waitKey(0) & 0xFF== ord('f'):
     break

video.release

cv2.destroyAllWindows()