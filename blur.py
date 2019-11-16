import cv2
import numpy

img=cv2.imread("lion.jpg")

blur1=cv2.GaussianBlur(img,(5,5),0)
blur2=cv2.blur(img,(5,5))
blur3=cv2.medianBlur(img,5)

cv2.imshow("img",blur3)
cv2.imshow("img1",img)

cv2.waitKey(0)
cv2.destroyAllWindows()