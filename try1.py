import cv2
import numpy as ny

cam=cv2.VideoCapture(0)
cat,fram=cam.read()
h,w,c=fram.shape
fram[(h/2):h,0:(w/2),]=225,150,118

cv2.imshow("image",fram)

cam.release()

cv2.waitKey()

cv2.destroyAllWindows()