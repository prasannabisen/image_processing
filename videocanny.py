import cv2
import numpy

cam=cv2.VideoCapture(0)

while(1):
    ret,img=cam.read()
    img=cv2.Canny(img,5,225)
    cv2.imshow("image",img)
    if(cv2.waitKey(1)==27):
        break

cam.release()
cv2.destroyAllWindows()