import numpy
import cv2

img=cv2.imread("lion.jpg")

ret,hol=cv2.threshold(img,127,225,cv2.THRESH_BINARY)
ret,hol1=cv2.threshold(img,127,225,cv2.THRESH_BINARY_INV)
ret,hol2=cv2.threshold(img,127,225,cv2.THRESH_TRUNC)
ret,hol3=cv2.threshold(img,127,225,cv2.THRESH_TOZERO)
ret,hol4=cv2.threshold(img,127,225,cv2.THRESH_TOZERO_INV)

cv2.imshow("image1",hol)
cv2.imshow("image2",hol1)
cv2.imshow("image3",hol2)
cv2.imshow("image4",hol3)
cv2.imshow("image5",hol4)

cv2.waitKey(0)
cv2.destroyAllWindows()