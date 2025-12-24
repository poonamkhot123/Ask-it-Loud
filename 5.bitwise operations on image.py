# bitwise operations imcludes AND.OR, NOT and XOR.
# it is most important and use for various purpose like masking.
# and find roi(region of interest) which is in complex shape.

import cv2
import numpy as np

img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.circle(img1,(100,100),100,
                     (255,255,255),-1)

img2 = np.zeros((250,500,3),np.uint8)
img2 = cv2.rectangle(img2,(10,10),(170,190)
                     ,(255,255,255),-1)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)

bitAnd = cv2.bitwise_and(img2,img1)
bitOr = cv2.bitwise_or(img2,img1)
bitnot = cv2.bitwise_not(img1)
bitXor = cv2.bitwise_xor(img1,img2)

cv2.imshow("bitAND",bitAnd)
cv2.imshow("bitOr",bitOr)
cv2.imshow("bitnot",bitnot)
cv2.imshow("Xor",bitXor)

cv2.waitKey(0)
cv2.destroyAllWindows()