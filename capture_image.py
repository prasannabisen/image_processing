import numpy
import cv2

for i in range(4):
    cap=cv2.VideoCapture(0)
    cat,fram=cap.read()
    cv2.imshow("image",fram)
    cap.release()
    cv2.waitKey(0)
    
cv2.destroyAllWindows()