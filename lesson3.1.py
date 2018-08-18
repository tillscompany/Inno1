import  cv2
color_image=cv2.imread("db/flower.jpg")
# BGR хранит
print(color_image.shape)
cv2.imshow('Color all',color_image)
cv2.imshow('Color blue',color_image[:,:,0])
cv2.imshow('Color green',color_image[:,:,1])
cv2.imshow('Color red',color_image[:,:,2])
cv2.waitKey(0)
#мы можем изменить цветовое постранство и попробовать отобразить изображение в RGB
color_image_rgb=cv2.cvtColor(color_image,cv2.COLOR_BGR2RGB)
cv2.imshow('Color RGB',color_image_rgb)
cv2.imshow('Color BGR',color_image)
cv2.waitKey(0)
color_spaces=('RGB','GRAY','HSV','LAB','XYZ','YUV')#все доступные
color_images={color:cv2.cvtColor(color_image,getattr(cv2,'COLOR_BGR2'+color))
              for color in color_spaces}
color_images={}
for color in color_spaces:
    color_images[color]=cv2.cvtColor(color_image,getattr(cv2,'COLOR_BGR2'+color))
for color in color_images:
    cv2.imshow(color,color_images[color])
    cv2.waitKey(0)
