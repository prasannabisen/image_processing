import cv2
import numpy

cap=cv2.VideoCapture(0)

rat,fram=cap.read()
cv2.imshow("image",fram)
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

