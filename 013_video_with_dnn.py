# coding=utf-8
# Источник: https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/

from imutils.video import VideoStream
import numpy as np
import imutils
import time
import cv2


# загрузим предобученную модель
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe("013_data/deploy.prototxt.txt", "013_data/res10_300x300_ssd_iter_140000.caffemodel")

# инициализируем видеострим и поставимнебольшую задержку, чтобы камера "поймала" изображение
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
cap = cv2.VideoCapture(0)
time.sleep(2.0)

# проверим, успешно ли произошло открытие камеры
if cap.isOpened() == False:
    print("Ошибка при открытии камеры!")

cv2.namedWindow('Window')
cv2.moveWindow('Window', 75, 75)

# будем выполнять цикл, пока не нажмем на кнопку для выхода из программы
while True:
    # считаем кадр и отресайзим его
    # сделаем ширину кадра 1024 пикселей
    frame = vs.read()
    frame = imutils.resize(frame, width=1024)

    # получим разрешение кадра и конвертируем его в blob
    """
        Для получения (правильных) прогнозов с помощью глубоких нейронных сетей сначала нужно предварительно обработать 
        входные данные. В контексте глубокого обучения и классификации изображений эти задачи предварительной обработки 
        обычно включают вычитание среднего и масштабирование по некоторым параметрам
    
        метод blobFromImage создает 4-мерный BLOB (англ. Binary Large Object — двоичный большой объект) из изображения. 
        Опционально изменяет размеры и обрезает изображение, вычитает среднее, шкалирует по шкале факторизации, 
        свопает синий и красный каналы.
        
        Подробнее можно почитать (на англ): 
            https://www.pyimagesearch.com/2017/11/06/deep-learning-opencvs-blobfromimage-works/
    """
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), scalefactor=1.0,
                                 size=(300, 300), mean=(104.0, 177.0, 123.0), swapRB=True)

    # подаем полученный blob объект на вход нейронной сети и получаем детекшены лиц и уверенность
    net.setInput(blob)
    detections = net.forward()

    # пройдемся по списку обнаруженных лиц
    for i in range(0, detections.shape[2]):
        # присвоим переменной уверенность/вероятность (confidence, probability) того, что обнаружено именно лицо
        confidence = detections[0, 0, i, 2]

        # отфильтруем детекшены с низкой уверенностью (< 0.5)
        if confidence < 0.5:
            continue

        # найдем (x, y)-координаты прямоугольников, обрамляющих лица
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        # нарисуем прямоугольники и вероятность
        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY),
                      (0, 0, 255), 2)
        cv2.putText(frame, text, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

    # выведем измененный кадр
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # если была нажата клавиша "q",то завершим вывод видео
    if key == ord("q"):
        break

# закрываем все окна
cv2.destroyAllWindows()
# vs.stop()