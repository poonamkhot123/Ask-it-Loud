# creating image border.
# with the help of cv2.copyMakeBorder() function.
# it take parameters like(img,border_width(4-sides),bordertype,val_border)
# border width = top,bottom,right,left.

import cv2
import numpy as np

img1 = cv2.imread("Amazon logo.jpg")

# creating image border.
brdr = cv2.copyMakeBorder(img1,15,15,5,5,cv2.BORDER_CONSTANT,
                          value = [255,0,125])

cv2.imshow("result",brdr)
cv2.waitKey(0)
cv2.destroyAllWindows()