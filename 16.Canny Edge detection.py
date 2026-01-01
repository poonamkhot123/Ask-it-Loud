"""
canny Edge Detection using openCV
canny edge Detection is a popular edge detection approach.
It is use multi-stage algorithm to detect a edges.
It was developed bhy John F.Canny in 1986

# this approach combine with 5 steps.
1) Noise reduction(guass)
2) Gradient calculation
3) Non maximum suppresson
4) Double Threshold
5) Edgr Tracking by Hysteresis.
"""

import cv2
import numpy as np

# to find which edge (x,y) is suitable lets create trackbar , thats why below code is comment out.
# load image into gray scale.
"""img = cv2.imread("chota bhim image.jpg")
img = cv2.resize(img,(600,500))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# canny(img,thresh1,thresh2) thresh1 and thresh2 at different level.
canny = cv2.Canny(img_gray,50,100)

cv2.imshow("Original==",img)
cv2.imshow("gray==",img_gray)
cv2.imshow("canny==",canny)"""

# load image into gray scale.
img = cv2.imread("chota bhim image.jpg")
img = cv2.resize(img,(600,500))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def nothing(x):
    pass

cv2.namedWindow("Canny")
cv2.createTrackbar("Threshold","Canny",0,255,nothing)

while True:
    a = cv2.getTrackbarPos("Threshold","Canny")
    print(a)
    result = cv2.Canny(img_gray,a,255)

    cv2.imshow("Canny",result)

    k = cv2.waitKey(1) & 0XFF
    if k == 27:
        break

cv2.destroyAllWindows()
