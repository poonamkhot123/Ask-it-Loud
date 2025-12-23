# image operations with pixels and cordinates.

import cv2
import numpy as np

# Read an image--
img = cv2.imread("Amazon logo.jpg")
img = cv2.resize(img,(400,200))

# image size we get.
print("shape==",img.shape)
print("No. of pixels==",img.size)
print("datatype==",img.dtype)
print("Imagetype==",type(img))


# Now try to split image.
# split - retrun 3 chanels of ur image
# print(cv2.split(img))

b,g,r = cv2.split(img)

cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)



cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()