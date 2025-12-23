import cv2

camera = "http://192.168.0.110:8080/video"

cap = cv2.VideoCapture(0)
cap.open(camera)
print("check===",cap.isOpened())

fourcc = cv2.VideoWriter_fourcc(*"XVID")

output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(700,700))
        cv2.imshow("Colorframe",frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cap.release()
output.release()
cv2.destroyAllWindows()