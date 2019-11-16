import cv2
import numpy

img=cv2.imread("lion.jpg")

m=numpy.float32([[1,0,100],[0,1,50]])
print (m)

h,w,c=img.shape

m=cv2.getRotationMatrix2D((h/2,w/2),90,1)
dst=cv2.warpAffine(img,m,(h,w))

cv2.imshow("image",img)
cv2.imshow("image1",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()