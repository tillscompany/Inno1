#import required libraries
#import OpenCV library
import cv2
#import matplotlib library
import matplotlib.pyplot as plt
#importing time library for speed comparisons of both classifiers
import time
import numpy as np
cv2.namedWindow('Window')
cv2.moveWindow('Window',75,75)
def detect_faces(f_cascade,colored_img,scaleFactor=1.1):
    img_copy=np.copy(colored_img)
    gray=cv2.cvtColor(img_copy,cv2.COLOR_BGR2GRAY)
    faces=f_cascade.detectMultiScale(gray,scaleFactor=scaleFactor,minNeighbors=5)
    for (x,y,w,h)in faces:
        cv2.rectangle(img_copy,(x,y),(x+w,y+h),(0,255,0),2)
    return img_copy
face_cascade=cv2.CascadeClassifier('lbpcascade_frontalface.xml')
cap=cv2.VideoCapture(0)
time.sleep(2.0)

if cap.isOpened()==False:
    print("ошибка при открытии камеры")
while (cap.isOpened()):
    # считываем кадр
    ret, frame = cap.read()
    if ret == True:
        frame=detect_faces(face_cascade,frame)

        cv2.imshow('Window', frame)
        # если была нажата кнопка q то завершим вывод
        button = cv2.waitKey(1) & 0x77
        if button == ord("q"):
            break
    # если кадры закончились то выйдем из цикла
        # когда закончим работу с видео, освобождаем переменную
cap.release()
# закрываем все окна