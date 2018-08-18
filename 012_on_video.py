import cv2
import numpy as np
import time


def detect_faces(f_cascade, colored_img, scaleFactor=1.1):
    img_copy = np.copy(colored_img)

    # конвертируем изображение в ЧБ, т.к. opencv face detector принимает ЧБ изображения
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

    # Теперь найдем лица на фото с помощью функции detectMultiScale
    faces = f_cascade.detectMultiScale(gray, scaleFactor=scaleFactor,
                                       minNeighbors=5)

    # пройдемся по списку и нарисуем прямоугольники у найденных лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return img_copy


#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')

cap = cv2.VideoCapture(0)
time.sleep(2.0)

# проверим, успешно ли произошло открытие камеры
if cap.isOpened() == False:
    print("Ошибка при открытии камеры!")

cv2.namedWindow('Window')
cv2.moveWindow('Window', 75, 75)

# будем выполнять цикл, пока не нажмем на кнопку для выхода из программы
while cap.isOpened():
    # считаем кадр (будем также называть его frame)
    ret, frame = cap.read()
    if ret:
        frame = detect_faces(face_cascade, frame)
        # отобразим кадр
        cv2.imshow('Window', frame)

        # если была нажата клавиша "q",то завершим вывод видео
        button = cv2.waitKey(1) & 0xFF
        if button == ord("q"):
            break

# когда мы закончили работать с видео, освобождаем переменную
cap.release()

# закрываем все окна
cv2.destroyAllWindows()

