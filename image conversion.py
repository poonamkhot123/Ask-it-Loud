# image conversion project colored into gray scale.
import cv2
path = input("Enter the path of the image:")
print("you enter this:",path)

# now read image
img1= cv2.imread(path,0)


cv2.imshow("image covergen.jpg",img1)

"""k = cv2.waitKey(0)
if k==ord("s"):
    cv2.imwrite("amazon image.jpg",img1)
else:
    cv2.destroyAllWindows()"""

cv2.waitKey(0)
cv2.destroyAllWindows()