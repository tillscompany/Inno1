import  cv2
cat_image=cv2.imread("db/cat.jpg")
cv2.imshow('Cat1',cat_image)
cv2.waitKey(0)
low_red=(17,50,110)#задаем диапазон который будем задавать,чтобы выделить кота
high_red=(101,140,180)
only_cat=cv2.inRange(cat_image,low_red,high_red)
cv2.imshow('Cat',only_cat)
cv2.waitKey(0)
#переводим изобрфжение в hsv чтобы выделить диапазон и выделить кота лучше
cat_image_hsv=cv2.cvtColor(cat_image,cv2.COLOR_BGR2HSV)
cat_color_low=(7,40,60)
cat_color_high=(18,255,200)
only_cat_hsv=cv2.inRange(cat_image_hsv,cat_color_low,cat_color_high)
cv2.imshow('only_cat_hsv',only_cat_hsv)
cv2.waitKey(0)
# отметим кота в кадре,ищем моменты где есть белый цвет(кот) и пишем текст там где нашли кота
moments=cv2.moments(only_cat_hsv,1)
x_moment=moments['m01']
y_moment=moments['m10']
area=moments['m00']
x=int(x_moment/area)
y=int(y_moment/area)
cv2.putText(cat_image,'cat!',(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.imshow('cat found',cat_image)
cv2.waitKey(0)