import cv2
import numpy

img=cv2.imread("lion.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,th=cv2.threshold(gray,125,225,cv2.THRESH_BINARY)

m=cv2.moments(th,True)

print(m)

hu=cv2.HuMoments(m)

print(hu)