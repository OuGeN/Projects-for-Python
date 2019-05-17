import cv2
import numpy as np

video=cv2.VideoCapture('RISE.mp4')

dgsm=cv2.createBackgroundSubtractorMOG2()

while(True):
    ret, frame=video.read()

    if ret:
        dgsmmask=dgsm.apply(frame)
        cv2.imshow('Hareket Algilama', dgsmmask)

        if cv2.waitKey(30) & 0xFF==27:
            break

video.release()
cv2.destroyAllWindows()




