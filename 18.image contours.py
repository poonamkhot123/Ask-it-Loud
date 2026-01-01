# Contours.
"""
Contours can be explained simply as a curve joining all the continuous points
(along the boundary),having same color or intensity.
The contours are a useful tool for shape analysis and object detection and

For better accuracy,use binary images and also apply edge detection before
finding contours.

findContour function manipulate original image so copy it before preceeding.
findContour is like finding white object from black background.

we have to find and draw contours as per the requirements.
"""

import cv2
import numpy as np

img = cv2.imread("doremon.jpg")
img = cv2.resize(img,(400,300))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img1 = cv2.resize(img1,(400,300))
ret,thresh = cv2.threshold(img1,120,255,0)

#findcontour(img,contour_retrival_mode,method)
cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(cnts,len(cnts))

#Drawcontour(img,cnts,id of contour,color,thickness)
#contour just pass -1
#Draw the contours
img = cv2.drawContours(img,cnts,10,(175,100,15),4)



cv2.imshow("Originla==",img)
cv2.imshow("gray==",img1)
cv2.imshow("thresh==",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()