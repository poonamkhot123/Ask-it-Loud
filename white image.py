import numpy as np
import cv2

image = np.ones([512,512,3],np.uint8)*255

cv2.imshow("white image.jpg",image)


cv2.waitKey(0)
cv2.destroyAllWindows()

