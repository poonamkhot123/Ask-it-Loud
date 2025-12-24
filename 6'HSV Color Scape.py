# HSV = Hue saturation value

# detect color in an image.

import cv2
import numpy as np

frame = cv2.imread("plastic-color-balls.jpg")
frame = cv2.resize(frame,(600,400))

while True:
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    upper_value = np.array([10,8,228])
    lower_value = np.array([11,246,241])

    # Creating mask
    mask = cv2.inRange(hsv,upper_value,lower_value)

    # filter mask with image.
    result = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()