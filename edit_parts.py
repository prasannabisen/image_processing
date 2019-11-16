import cv2
import numpy

img=cv2.imread("lion.jpg")

print(img.shape)
h,w,c=img.shape
leftHalf=img[(h/2):,(w/2):,]

cv2.imshow("image",leftHalf)
cv2.waitKey(0)

cv2.destroyAllWindows()