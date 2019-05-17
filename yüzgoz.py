import cv2
import numpy as np


face=cv2.CascadeClassifier('Dataset/haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier('DataSet/haarcascade_eye.xml')
foto=cv2.imread('Arrow.jpg',0)
gri=cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
faces=face.detectMultiScale(gri,1.3,5)


for(x,y,w,h) in faces:
    cv2.rectangle(foto, (x,y), (x+w, y+h), (255,0,0),2)
    gray=gri[y:y+h, x:x+w]
    color=foto[y:y+h, x:x+w]


    eyes=eye.detectMultiScale(gray)

    for(ex, ey, ew, eh) in eyes:
        cv2.rectangle(color, (ex,ey), (ex+ew+eh),(10,255,0),2)

        cv2.imshow('Yuz ve Goz', foto)
        cv2.waitKey(0)
        cv2.destroyAllWindows()