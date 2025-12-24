# image smoothning and blurring.
"""
Image smoothing or bluring is most common used operation in Image Processing.
It is use to remove noise from the images.
There are so many filter which is use for smoothing the image.
There are Low pass filter(LPS) which use to remove Noise from the images.
There are High pass filter which use to detect and finding edges in an image.
"""
 # We discuss about various filters --
 # Like , homogeous,blur(averaging),guassian,median,bilateral.

import cv2
import numpy as np

img = cv2.imread("chota bhim image.jpg")
img = cv2.resize(img,(500,600))
cv2.imshow("original==",img)


kernel = np.ones((2,2),np.float32)/4


# 1) Homogeneous Filter.
"""
This filter work like,each output pixel is the mean of its kernal neighbour
it is aka homogeneous filter in this all pixel acontribute with equal weight.
kernal is a small shape or matrix which we apply on image.
In this filter kernal is [(1/kernal(h,w)*kernal)].
"""
h_filter = cv2.filter2D(img,-1,kernel) # -1 is desired depth.
cv2.imshow("homogeneous",h_filter)

# 2) Blur Method or Averanging filter.
""""
Takes the average of all the pixels under kernel area and
replaces the central element with this average.
"""
blur = cv2.blur(img,(8,8)) # Here we have image and kernel as parameter.
cv2.imshow("blur==",blur)

# 3) Gaussian blur Filter.
"""
Here it using different weight kernel, in row as well as column
means side values are small  then centre.It manage distance b/w value of pixel.
"""
gau = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("gau blur",gau)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 4) Median blur filter.
"""
computes the median of all the pixels under the kernel window and cental pixel
is replaced with this medain value.
This is highly effective in removing salt and peppaer noise.
here kernal size must be odd except one.
"""
med = cv2.medianBlur(img,5)
cv2.imshow("median filter",med)


# 5) bilateral filter.
"""
It work like gaussian filter but more focus on edges
it is slow as compare with other filters
argument(img,neighbour_pixel_diameter,sigma_color,sigma_space)
"""
bi_f = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("bi_f",bi_f)

cv2.waitKey(0)
cv2.destroyAllWindows()

