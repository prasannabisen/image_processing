import cv2
import numpy

cap=cv2.VideoCapture(0)

while(1):
    cat,fram=cap.read()
    h,w,c=fram.shape
    fram[(h/2):h,(w/2):w,]=225
    cv2.imshow("image",fram)    
    if(cv2.waitKey(1)==27):
        break

cap.release()
cv2.destroyAllWindows()
