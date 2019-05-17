import cv2
import numpy as np

photo=cv2.imread('kata.jpg',0)
cv2.imshow('MY MAIN KATARINA',photo)

a=cv2.waitKey(0) & 0xFF
if a==27:
    cv2.destroyAllWindows()

elif a== ord('g'):
    cv2.imwrite('katagri.png',photo)
    cv2.destroyAllWindows()
