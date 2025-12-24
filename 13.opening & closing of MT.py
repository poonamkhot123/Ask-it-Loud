# Morphological transformations are some simple operations based on the image shape.
"""
it is normally performed on binary images.
it needs two inputs - 1) original image , 2)- strucuring element(kernel).
two more basic morphological transformations are
1) Opening and 2) Closing.

"""
import cv2
import numpy as np
# opening--
# opening is just another name od erosion followed by dilation.
# means first erosion take place then dilation.

img = cv2.imread("chota bhim image.jpg",0)
img = cv2.resize(img,(600,400))

_,mask = cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((4,4),np.uint8) # 5x5 kenerl with of ones.
o = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel) #optional parameters iterations = 2.

cv2.imshow("img",img)
cv2.imshow("ker==",kernel)
cv2.imshow("mask==",mask)
cv2.imshow("openings==",o)

# Closing.
"""
It is opposite of opening
closing is just another name of dilation followed by erosion.
means first dilation take place then erosion.
"""

kernel = np.ones((3,3),np.uint8) # 5x5 kernel with full of ones.
c = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
cv2.imshow("closing",c)


cv2.waitKey(0)
cv2.destroyAllWindows()
