# image pyramid in openCV.
"""
We use Image Pyramid beacuase somethings we work on same image
but different resolutio.e.g searching face,eye in an image
and it vary image so in this case we create a set of images
with diff. resolution which is called pyramid.
We also use these pyramids to blends the images.
"""

# There are two types of Image Pyramid.
# 1) Guassian Pyramid and 2) Laplacian Pyramids.

import cv2
import numpy as np

# load Image into gray scale.
img = cv2.imread("doremon.jpg")
img = cv2.resize(img,(600,400))

# Guassian pyramid have 2 functions.
"""
1) cv2.pyrUp()
2) cv2.pyrDown()
"""

# pyramid down
pd1 = cv2.pyrDown(img)
pd2 = cv2.pyrDown(pd1)

#pyrup
pu1 = cv2.pyrUp(pd2)   # starts from small image.
pu2 = cv2.pyrUp(pu1)

cv2.imshow("Original==",img)
cv2.imshow("pd1",pd1)
cv2.imshow("pd2",pd2)
cv2.imshow("pu1",pu1)
cv2.imshow("pu2",pu1)

cv2.waitKey(0)
cv2.destroyAllWindows()


