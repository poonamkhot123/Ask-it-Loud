# now capture video from webcam and save into memory.

import cv2

cap = cv2.VideoCapture(0)
print(cap)

while cap.isOpened():
    ret,frame = cap.read()
    frame = cv2.resize(frame,(700,450))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame",frame)
    cv2.imshow("gray",gray)
    k = cv2.waitKey(100)

    if k == ord("q") & 0xFF:
        break
    
cap.release()
cv2.destroyAllWindows()
