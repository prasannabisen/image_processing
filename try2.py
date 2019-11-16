import cv2
import numpy as ny

image=cv2.imread("lion.jpg")
h,w,c=image.shape
print(h)
print(w)
print(c)
image[(h/2):h,(w/2):w,2]=225
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()