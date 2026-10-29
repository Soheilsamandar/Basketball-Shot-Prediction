import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

video_path = "data/vid (4).mp4"
cap = cv2.VideoCapture(video_path)

myColorFinder = ColorFinder(trackBar=True)

hsvVals = {"hmin": 0, "smin": 0, "vmin": 0, "hmax": 179, "smax": 255, "vmax": 255}

paused = False
img = None

while True:

    if not paused:
        success, frame = cap.read()

        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        img = frame

    if img is not None:
        imgColor, mask = myColorFinder.update(img, hsvVals)

        imgStack = cvzone.stackImages([img, imgColor, mask], 3, 0.6)

        cv2.imshow("Color Finder", imgStack)

    key = cv2.waitKey(30) & 0xFF

    if key == 32:
        paused = not paused
        print("Paused" if paused else "Playing")

    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
