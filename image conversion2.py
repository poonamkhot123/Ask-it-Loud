import cv2

img1 = cv2.imread("output_python.jpg")


img1 = cv2.flip(img1,0)

cv2.imshow("amazon logo.jpg:",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()