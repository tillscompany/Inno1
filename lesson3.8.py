import  cv2
import numpy as np
cv2.namedWindow('window')
cv2.moveWindow('window',75,75)
hsv_min = np.array((2,28,65), np.uint8)
hsv_max = np.array((26,238,255), np.uint8)
file_path="db/donuts.jpg"
img=cv2.imread(file_path)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
thresh = cv2.inRange(hsv, hsv_min, hsv_max)

_,countours,hierarchy=cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,countours,-1,(255,0,0),3,cv2.LINE_AA,hierarchy,1)
cv2.imshow('window',img)
cv2.waitKey()
cv2.destroyAllWindows()