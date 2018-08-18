import cv2
import matplotlib.pyplot as plt
import time
import numpy as np
import os

subjects = ["", "Benedict", "Elena", "Alexandr Kolotov"]
face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')


def detect_faces(f_cascade, colored_img, scaleFactor=1.1):
    img_copy = np.copy(colored_img)
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    faces = f_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=5)
    if len(faces) == 0:
        return None, None
    (x, y, w, h) = faces[0]
    return gray[y:y + w, x:x + h], faces[0]


def rectangle(colored_img, coordinates):
    img_copy = np.copy(colored_img)
    x, y, w, h = coordinates
    cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return img_copy


def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
    return img


def draw_confidence(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
    return img


def my_resize(img, width=400):
    ratio = float(width) / img.shape[1]
    new_shape = (width, int(img.shape[0] * ratio))
    resized = cv2.resize(img, new_shape, interpolation=cv2.INTER_AREA)
    return resized


def predict(test_img):
    img = test_img.copy()
    face, rect = detect_faces(face_cascade, img)
    if face is None:
        return test_img
    label, confidence = face_recognizer.predict(face)
    if confidence < 45:
        label_text = subjects[label]
        img = rectangle(img, rect)
        img = draw_text(img, label_text, rect[0], rect[1] - 5)
        confidence_text = str(round(confidence, 3))
        img = draw_confidence(img, confidence_text, rect[0], rect[1] - 30)
    else:
        img = rectangle(img, rect)
        draw_text(img, "Unknown", rect[0], rect[1] - 5)
    return img


face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')


def prepare_training_data(data_folder_path):
    dirs = os.listdir(data_folder_path)
    faces = []
    labels = []
    for dir_name in dirs:
        if not dir_name.startswith("s"):
            continue
        label = int(dir_name.replace("s", ""))
        image_names = os.listdir(data_folder_path + "/" + dir_name)
        for file in image_names:

            if file.startswith("._"):
                continue
            else:
                i1 = cv2.imread(data_folder_path + "/" + dir_name + '/' + file)
                i2 = detect_faces(face_cascade, i1)
                if not i2[0] is None:
                    faces.append(i2[0])
                    labels.append(label)
    return faces, labels


faces, labels = prepare_training_data('train_data')
print('Total faces: ', len(faces))
print('Total labels: ', len(labels))
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))

time.sleep(2.0)
cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("ошибка при открытии камеры")
while (cap.isOpened()):
    # считываем кадр
    ret, frame = cap.read()
    if ret == True:
        cv2.namedWindow('biometry')
        cv2.moveWindow('biometry', 75, 75)
        frame = predict(frame)
        cv2.imshow('biometry', frame)
        # если была нажата кнопка q то завершим вывод
        button = cv2.waitKey(1) & 0x77
        if button == ord("q"):
            break
            # когда закончим работу с видео, освобождаем переменную
cap.release()
