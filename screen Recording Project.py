import cv2
import pyautogui as p
import numpy as np


# create resolution
rs = p.size()

# filename in which we store recording.
fn = input("Please enter any file name and path:")

# fix the the frame rate
fps = 60.0

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter(fn,fourcc,fps,rs)

# create recording module
cv2.namedWindow("Live_Recording",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live_Recording",(600,400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = cv2.cvtColor(f,cv2.COLOR_RGB2BGR)
    output.write(f)
    cv2.imshow("Live_Recording",f)
    
    if cv2.waitKey(1) == ord("q"):
        break

output.release()
cv2.destroyAllWindows()
