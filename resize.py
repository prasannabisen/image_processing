import numpy
import cv2

img=cv2.imread("lion.jpg")

h,w,c=img.shape
print(img.shape)
kk=cv2.resize(img,(h/2,w/2),interpolation=cv2.INTER_AREA)
cv2.imshow("image",kk)
print(kk.shape)
cv2.waitKey()
cv2.destroyAllWindows()