#------------- Gesture Control Media Player --------------

import cv2
import numpy as np
import math
import pyautogui as p
import time as t

# Read Camera.
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# 🔹 ADD VIDEO (DO NOT REMOVE pyautogui CONTROL)
video = cv2.VideoCapture("Video Player.mp4")  # keep video in same folder

def nothing(x):
    pass

# window name
cv2.namedWindow("Color Adjustments",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Color Adjustments",(300,300))
cv2.createTrackbar("Thresh","Color Adjustments",0,255,nothing)

# Color Detection Track
cv2.createTrackbar("Lower_H","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Lower_S","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Lower_V","Color Adjustments",0,255,nothing)

cv2.createTrackbar("Upper_H","Color Adjustments",255,255,nothing)
cv2.createTrackbar("Upper_S","Color Adjustments",255,255,nothing)
cv2.createTrackbar("Upper_V","Color Adjustments",255,255,nothing)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,2)
    frame = cv2.resize(frame,(600,500))

    # get hand data from rectangle
    cv2.rectangle(frame,(0,1),(300,500),(255,0,0),0)
    crop_image = frame[1:500,0:300]

    hsv = cv2.cvtColor(crop_image,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("Lower_H","Color Adjustments")
    l_s = cv2.getTrackbarPos("Lower_S","Color Adjustments")
    l_v = cv2.getTrackbarPos("Lower_V","Color Adjustments")

    u_h = cv2.getTrackbarPos("Upper_H","Color Adjustments")
    u_s = cv2.getTrackbarPos("Upper_S","Color Adjustments")
    u_v = cv2.getTrackbarPos("Upper_V","Color Adjustments")

    lower_bound = np.array([l_h,l_s,l_v])
    upper_bound = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv,lower_bound,upper_bound)
    filter = cv2.bitwise_and(crop_image,crop_image,mask=mask)

    mask1 = cv2.bitwise_not(mask)
    m_g = cv2.getTrackbarPos("Thresh","Color Adjustments")
    _, thresh = cv2.threshold(mask1,m_g,255,cv2.THRESH_BINARY)

    cnts,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    try:
        cm = max(cnts, key=cv2.contourArea)
        hull = cv2.convexHull(cm)

        cv2.drawContours(crop_image,[cm],-1,(50,50,150),2)
        cv2.drawContours(crop_image,[hull],-1,(0,255,0),2)

        hull_idx = cv2.convexHull(cm, returnPoints=False)
        defects = cv2.convexityDefects(cm, hull_idx)

        count_defects = 0
        for i in range(defects.shape[0]):
            s,e,f,_ = defects[i,0]
            start = tuple(cm[s][0])
            end = tuple(cm[e][0])
            far = tuple(cm[f][0])

            a = math.dist(start,end)
            b = math.dist(start,far)
            c = math.dist(end,far)

            angle = math.acos((b*b + c*c - a*a)/(2*b*c)) * 180 / math.pi
            if angle <= 50:
                count_defects += 1
                cv2.circle(crop_image,far,5,(255,255,255),-1)

        if count_defects == 1:
            p.press("space")
        elif count_defects == 2:
            p.press("up")
        elif count_defects == 3:
            p.press("down")
        elif count_defects == 4:
            p.press("right")

    except:
        pass

    # 🔹 VIDEO PLAYBACK (ADDED – DOES NOT AFFECT GESTURE LOGIC)
    ret_v, v_frame = video.read()
    if ret_v:
        v_frame = cv2.resize(v_frame,(640,360))
        cv2.imshow("Video Player", v_frame)
    else:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)

    cv2.imshow("Thresh", thresh)
    cv2.imshow("Filter", filter)
    cv2.imshow("Result", frame)

    if cv2.waitKey(25) & 0xFF == 27:
        break

cap.release()
video.release()   # 🔹 RELEASE VIDEO
cv2.destroyAllWindows()
