# Image gradient.
"""
It is a directional change i the color or intensity in an image.
It is most important part to find imnformation from image.
Like finding edges within the images.
There arevarious methods to find image gradient.
These are - Laplacian Derivatives,SobelX and SobelY.
All these functions have diff. mathematical approach to get result.
All load image in the gray scale.
"""

import cv2
import numpy as np

# load image into gray scale.
img = cv2.imread("doremon.jpg")
img = cv2.resize(img,(600,400))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# load image into gray scale.
# laplacian Derivative---It calculate Laplace derivative.
# parameter(img,data_type for -ve val,ksize)

lap = cv2.Laplacian(img_gray,cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))


# Sobel Operations.
"""
Is a joint Guassian smoothning plus differentiation operation,
so it is more resistant to noise
This is use for x and y both.
parameter(img,type for -ve val, x =1,y=0,ksize)
Sobel x focus on vertical lines.
Sobel y focus on horizontal lines.
"""

sobelX = cv2.Sobel(img_gray,cv2.CV_64F,1,0,ksize=3) # Here 1 means X direction.
sobelY = cv2.Sobel(img_gray,cv2.CV_64F,0,1,ksize=3) # Here 1 means y direction.

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# finally combine sobelX and sobelY together.
sobelcombine = cv2.bitwise_or(sobelX,sobelY)

cv2.imshow("original==",img)
cv2.imshow("gray==",img_gray)
cv2.imshow("sobelx.img",sobelX)
cv2.imshow("sobelY",sobelY)
cv2.imshow("Combined image==",sobelcombine)


cv2.waitKey(0)
cv2.destroyAllWindows()