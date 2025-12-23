# capture video from youtube.

import cv2
import pafy

url ="https://www.youtube.com/watch?v=PAuco4ehQUE&t=4692s"

data = pafy.new(url)
data = data.getbest(preftype = "mp4")

cap = cv2.VideoCapture(data.url)
cap.open(data.url)

print("check==",cap.isOpened() )

fourcc = cv2.VideoWriter_fourcc(*"XVID")

# it is 4 byte code which is use to specify the video codec
output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret,frame = cap.read() # here read the frame
    if ret == True:
        frame = cv2.resize(frame,(640,480))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Colourframe",frame)
        cv2.imshow("gray",frame)
        
        if cv2.waitKey(1) & 0xFF  == ord('q'):
            break

# release everything if job is finished.
cap.release()
output.release()
cv2.destroyAllWindows()