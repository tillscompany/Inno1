import cv2
import time
import os
NAME='s3'
path='train_data/{}'.format(NAME)
cv2.namedWindow("camera", 1)
if not os.path.exists(path):
    os.makedirs(path)
cap = cv2.VideoCapture(0)
i = 0
while (cap.isOpened()):
    # считываем кадр
    ret,img= cap.read()
    if ret == True:
        cv2.imshow("camera", img)
        button = cv2.waitKey(1) & 0x77
        if button == ord('s'):
            cv2.imwrite(path+'/'+"face-" + str(i)+'.jpg', img)
            i=i+1
        if cv2.waitKey(10) == 27:
            break