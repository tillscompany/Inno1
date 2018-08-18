import numpy as np
import cv2
cap = cv2.VideoCapture("db/winnie_video_1.mp4")
if cap.isOpened()==False:
    print("ошибка при открытии файла")

while(cap.isOpened()):
    #считываем кадр
    ret,frame=cap.read()
    if ret==True:
        cv2.imshow('Frame',frame)
        button = cv2.waitKey(50) & 0x77
        if button==ord("q"):
            break
    #если кадры закончились то выйдем из цикла
    else:
        break
#когда закончим работу с видео, освобождаем переменную
cap.release()
#закрываем все окна
cv2.destroyAllWindows()