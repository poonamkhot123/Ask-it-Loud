# Shi - Tomasi Corner Detector
"""
we will see the function: cv2.goodFeaturesToTrack().
Shi-Tomasi approach is more efficient as compared with Harris Corner detection.
In this we limit the number of corners and corners quality.
It is more user friendly.
"""

import numpy as np
import cv2
import matplotlib as plt

img = cv2.imread("Amazon logo.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# parameters(img,no.of corner,quality_level,min_distance between corner)
corners = cv2.goodFeaturesToTrack(gray,100,0.01,10)
corners = np.int64(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow("res==",img)
cv2.waitKey(0)
cv2.destroyAllWindows()