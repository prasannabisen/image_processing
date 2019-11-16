import numpy as np
import cv2

cap=np.zeros((400,400,3),np.uint8)
cv2.line(cap,(50,0),(400,0),(225,0,0),6)
cv2.rectangle(cap,(80,40),(300,100),(0,255,0),6)
cv2.circle(cap,(190,40),50,(0,0,225),3)
cv2.imshow("image",cap)

cv2.waitKey(0)
cv2.destroyAllWindows()
