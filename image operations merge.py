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

# Now if you want to mix the channels then use merge.
mr1 = cv2.merge((r,g,b))
cv2.imshow("rgb",mr1)

mr2 = cv2.merge((g,b,r))
cv2.imshow("gbr",mr2)
cv2.imshow("original",img)


cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()