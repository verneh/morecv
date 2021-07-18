# Testing Google's Mediapipe.
import cv2
import mediapipe as mp
import time

# to access webcam
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
# Utilities to draw landmarks and connectors.
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    # multi hand landmarks - performs precise keypoint localization 
    # of 21 3D hand-knuckle coordinates inside the detected hand regions 
    #  via regression, that is direct coordinate prediction.

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:
            # index number and landmark. find it in the hand.
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                # if id == 4:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Mediapipe", img)
    cv2.waitKey(1)
