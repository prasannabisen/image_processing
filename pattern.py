import cv2
import numpy as np

#######make image#############
image=np.zeros((400,400),np.uint8)

image[200:400,0:200]=225
image[:200,200:400]=225
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()