import cv2
import numpy as nu
########gray scale##############
img=cv2.imread("lionBMP.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

h,w,c=gray.shape

gray[(h/2):,0:(w/2)]=225

cv2.imshow("image",gray)


cv2.waitKey(0)

cv2.destroyAllWindows()