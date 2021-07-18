# a version that relies on our previous module.
import cv2
import mediapipe as mp
import time
import handtracking_module as htm

# We are calling functions from the HandTrackingModule

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True )
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[4])
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
     #           (255, 0, 255), 3)
    cv2.imshow("Hand Tracking", img)
    cv2.waitKey(1)

