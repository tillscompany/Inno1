import cv2
cv2.namedWindow('window')
cv2.moveWindow('window',75,75)
cap=cv2.VideoCapture(0)
if cap.isOpened()==False:
    print("ошибка при открытии камеры")
#считываем разрешение экрана
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
#
out=cv2.VideoWriter("db/outpy.avi",cv2.VideoWriter_fourcc('M','J','P','G'),10,(frame_width,frame_height))
while (cap.isOpened()):
    # считываем кадр
    ret, frame = cap.read()
    if ret == True:
        #запишем кадр в
        out.write(frame)
        cv2.imshow('Window', frame)
        # если была нажата кнопка q то завершим вывод
        button = cv2.waitKey(25) & 0x77
        if button == ord("q"):
            break
    # если кадры закончились то выйдем из цикла
    else:
        break
        # когда закончим работу с видео, освобождаем переменную
cap.release()
# закрываем все окна