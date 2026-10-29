import cv2 as cv
import numpy as np
import cvzone
import math


data = "data/vid (6).mp4"
cap = cv.VideoCapture(data)


posListX, posListY = [], []
xList = []
for i in range(0, 1300):
    xList.append(i)
frame_counter = 1
true_list = []
fc_true = []
fc_false = []


def resize(frame, perc=40):
    width = int(frame.shape[1] * perc / 100)
    height = int(frame.shape[0] * perc / 100)
    dim = (width, height)
    res = cv.resize(frame, dim, interpolation=cv.INTER_AREA)
    return res



lower = np.array([10, 160, 115])
upper = np.array([14, 255, 255])

while True:
    ret, frame = cap.read()
    if ret is False:
        break
    frame = frame[0:900, :]
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv_frame, lower, upper)
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    if contours:
        for cnt in contours:
            if cv.contourArea(cnt) > 505:
                x, y, w, h = cv.boundingRect(cnt)
                cnt_x = int(x + w // 2)
                cnt_y = int(y + h // 2)
                posListX.append(cnt_x)
                posListY.append(cnt_y)
    if len(posListX) >= 3:
        # Polynomial Regression y = Ax^2 + Bx + C
        A, B, C = np.polyfit(posListX, posListY, 2)
        for i in range(len(posListX)):
            pos = (posListX[i], posListY[i])
            cv.circle(frame, pos, 5, (0, 0, 255), cv.FILLED)
            if i > 0:
                cv.line(frame, pos, (posListX[i - 1], posListY[i - 1]), (0, 255, 0), 1)
        # Draw prediction curve
        for x in xList:
            y = int(A * x**2 + B * x + C)
            if 0 <= y < frame.shape[0]:
                cv.circle(frame, (x, y), 2, (255, 0, 255), 1)

        ### Prediction the ball path to see if it will go into the basket area
        # Basket area: X values 330 to 430, Y = 590
        a = A
        b = B
        c = C - 590  # height of the basket
        if abs(a) > 0:
            disc = b**2 - 4 * a * c
            if disc >= 0:
                x1 = (-b + math.sqrt(disc)) / (2 * a)
                x2 = (-b - math.sqrt(disc)) / (2 * a)
                # Choose the root that is more likely to be in frame
                if 0 < x1 <= 1300:
                    xPred = x1
                else:
                    xPred = x2
                prediction = 330 < xPred < 430
        else:
            prediction = False
        if prediction:
            cvzone.putTextRect(
                frame,
                "Basket",
                (50, 150),
                scale=5,
                thickness=5,
                colorR=(0, 200, 0),
                offset=20,
            )
        else:
            cvzone.putTextRect(
                frame,
                "No Basket",
                (50, 150),
                scale=5,
                thickness=5,
                colorR=(0, 0, 200),
                offset=20,
            )
    frame = resize(frame, 40)
    frame_counter += 1
    cv.imshow("vid", frame)
    if cv.waitKey(80) == 27:
        break
