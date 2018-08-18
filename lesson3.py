import cv2

image=cv2.imread("db/Winnie.jpg")
cv2.imshow("Resized image",image)
cv2.waitKey(0)
print("Image shape",image.shape)

#resized=cv2.resize(image, (250, 398))

new_width=200
#масштабируем изображение
ratio=float(new_width)/image.shape[1]
new_shape=(new_width,int(image.shape[0]*ratio))
resized=cv2.resize(image, new_shape,interpolation=cv2.INTER_AREA)
cv2.imshow("Resized image",resized)
cv2.waitKey(0)
print("New image shape",resized.shape)
#обрезаем изображение
cropped =image[150:520,280:525]
cv2.imshow("Cropped image",cropped)
print("Cropped image shape",cropped.shape)
cv2.waitKey(0)
#поворачиваем изображение на 180 градусов
(h,w)=image.shape[:2]
center=(w/2,h/2)#выделение центра изображения
M=cv2.getRotationMatrix2D(center,180,1.0)
rotated=cv2.warpAffine(image,M,(w,h))
cv2.imshow("Rotated image",rotated)
cv2.waitKey(0)
#отражение относительно осей,0-по вертикали, 1 по горизонтали, -1 - по вертикали и горизонтали
flip_image=cv2.flip(image,1)
cv2.imshow("Rotated image",flip_image)
cv2.waitKey(0)
cv2.imwrite("db/Rotatedimage.jpg",flip_image)