import cv2
import numpy as np

img = cv2.imread("Amazon logo.jpg")

# ROI = region of interest.

# (186,160)   (346,267)
# [(y1:y2),(x1:x2)]
# y= y2-y1 = 107 ( height of img)
# x = x2-x1 = 160  ( width of img)

roi = img[160:267,186:346]

# now passing data into img.
img[160:267,347:507] = roi
img[160:267,508:668] = roi
img[160:267,25:185]  = roi

# changing in y
img[0:107,150:310] = roi


cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()