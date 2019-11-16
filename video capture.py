import cv2
import numpy

cap=cv2.VideoCapture(0)

while (1):
    cat,img=cap.read()
    cv2.imshow("image",img)
    if(cv2.waitKey(1)==27):
        break

cap.release()
cv2.destroyAllWindows()
