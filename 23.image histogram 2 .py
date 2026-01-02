# Create a Histogram for Colorfull image.

import numpy as np
import matplotlib.pyplot as plt
import cv2

# with color image.
img = cv2.imread("chota bhim image.jpg")
img = cv2.resize(img,(400,300))

b,g,r = cv2.split(img)

cv2.imshow("img",b)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)

# plotting different channel with hist.
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

plt.title("Colorfull Image")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
