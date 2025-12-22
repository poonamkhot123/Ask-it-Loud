import cv2

image = cv2.imread("output_python.jpg")

cv2.imshow("original",image)

cv2.waitKey(0)
cv2.destroyAllWindows()