# draw date time and figures on video

import cv2
import datetime


cap = cv2.VideoCapture(r"C:\Users\POONAM KHOT\OneDrive\Documents\Image processing and OpenCV\video.avi")

print("for width===",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("for height===",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("width====",cap.get(3))
print("Height===",cap.get(4))


while(cap.isOpened()):
    ret,frame = cap.read()

    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        text = "Height:" + str(cap.get(4))+'width:'+str(cap.get(3))
        frame = cv2.putText(frame,text,(10,20),font,1,(0,155,255),1,cv2.LINE_AA)

        date_data = "Date:"+str(datetime.datetime.now())
        frame = cv2.putText(frame,date_data,(20,50),font,1,(100,5,255),1,cv2.LINE_AA)




        cv2.imshow("frame",frame)

        if cv2.waitKey(30) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()