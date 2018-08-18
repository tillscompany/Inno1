import numpy as np
import cv2

def create_path(img):
    h,w=img.shape[:2]
    return np.zeros((h,w,3),np.uint8)
cv2.namedWindow('Frame')
cv2.moveWindow('Frame',75,75)
cap=cv2.VideoCapture(0)
if cap.isOpened()==False:
    print("ошибка при открытии камеры")
#считываем разрешение экрана
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
hsv_min = np.array((53,55,147), np.uint8)
hsv_max = np.array((83,160,255), np.uint8)
lastx=0
lasty=0
path_color=(0,0,255)
flag,img=cap.read()
path_img=create_path(img)
x=0
y=0
while(cap.isOpened()):
    #считываем кадр
    ret,frame=cap.read()
    if ret==True:
        #если была нажата кнопка q то завершим вывод
        image_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        only = cv2.inRange(image_hsv, hsv_min, hsv_max)
        moments = cv2.moments(only, 1)
        x_moment = moments['m01']
        y_moment = moments['m10']
        area = moments['m00']

        if area>100:
            x=int(y_moment/area)
            y=int(x_moment/area)
            cv2.circle(frame, (x, y), 10, (153, 100, 39), -1)
        if lastx >0 and lasty>0:
            cv2.line(path_img,(lastx,lasty),(x,y),path_color,5)

        lastx=x
        lasty=y
        img=cv2.add(frame,path_img)
        cv2.imshow('Frame',img)
        button = cv2.waitKey(1) & 0x77
        if button==ord("q"):
            break

cap.release()
#закрываем все окна
cv2.destroyAllWindows()