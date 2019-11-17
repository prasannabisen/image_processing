import cv2
import numpy

img=cv2.imread("shape.png")
cv2.imshow("org",img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("image",img)
ret,img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("image1",img)
img=cv2.Canny(img,25,225)
cv2.waitKey(0)
cv2.destroyAllWindows()