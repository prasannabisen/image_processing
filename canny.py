import cv2
import numpy

img=cv2.imread("lion.jpg")
kk=cv2.Canny(img,127,225)
cv2.imshow("image",kk)
cv2.waitKey(0)
cv2.destroyAllWindows()