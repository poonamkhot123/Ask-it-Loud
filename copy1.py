import cv2
import pafy

url = "https://www.youtube.com/watch?v=HJFxTsX0Ok0"

video = pafy.new(url)
best = video.getbest(preftype="mp4")

cap = cv2.VideoCapture(best.url)

print("Check =", cap.isOpened())

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        output.write(frame)

        cv2.imshow("Color Frame", frame)
        cv2.imshow("Gray Frame", gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
output.release()
cv2.destroyAllWindows()
