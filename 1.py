##################import open cv############
import numpy
import cv2
#############################################

#################read image###################

img=cv2.imread("lionBMP.jpg")
img2=cv2.imread("lion.jpg")

###########do processing##############
############################

##############show image#################
cv2.imshow("image",img)
cv2.imshow("image1",img2)

#######################close and exit##############3

cv2.waitKey(0)
cv2.destroyAllWindows()
