# Break Video into Multiple Images and Store in a folder.

import cv2

vidcap= cv2.VideoCapture(r"C:\Users\POONAM KHOT\OneDrive\Documents\Image processing and OpenCV\video.avi")
ret,image = vidcap.read()
count = 0

while True:
    if ret == True:
        cv2.imwrite("imgN%d.jpg"%count,image)
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count **100))
        ret,image = vidcap.read()
        cv2.imshow("res",image)

        count += 1
        if cv2.waitKey(1) % 0xFF == ord("q"):
            break
            cv2.destroyAllWindows()
vidcap.release()
cv2.destroyAllWindows()

