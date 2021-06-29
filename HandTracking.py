"""
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
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

    cv2.imshow("Image", img)
    cv2.waitKey(1)
"""

import cv2 as cv
import mediapipe as mp
import time


class HandDetector:
    def __init__(self, mode, max_hands, detection_conf, tracking_conf):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=mode,
                                         max_num_hands=max_hands,
                                         min_detection_confidence=detection_conf,
                                         min_tracking_confidence=tracking_conf)
        self.mp_draw = mp.solutions.drawing_utils
        self.current_time = 0
        self.previous_time = 0

    def draw_specific(self, image, points=None):
        h, w, c = image.shape
        image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        result = self.hands.process(image_rgb)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                for ids, landmarks in enumerate(hand_landmarks.landmark):
                    if points is not None:
                        for point in points:
                            cx, cy = int(landmarks.x * w), int(landmarks.y * h)
                            if ids == point and points is not None:
                                cv.circle(image, (cx, cy), 5, (255, 0, 255), -1)
        return image

    def get_specific_coordinates(self, image, points=None):
        h, w, c = image.shape
        image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        result = self.hands.process(image_rgb)
        temp = []
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                for ids, landmarks in enumerate(hand_landmarks.landmark):
                    if points is not None:
                        for i in points:
                            if ids == i:
                                cx, cy = int(landmarks.x * w), int(landmarks.y * h)
                                temp.append([ids, cx, cy])
        return temp

    def draw_all(self, image):
        image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        result = self.hands.process(image_rgb)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return image

    def get_fps(self):
        self.current_time = time.time()
        f = round(1 / (self.current_time - self.previous_time), 2)
        self.previous_time = self.current_time
        return f


# cap = cv.VideoCapture(0)
# hd = HandDetector(False, 2, 0.5, 0.5)
# while True:
#     _, img = cap.read()
#     img = hd.draw_all(img)
#     id_x_y_array = hd.get_specific_coordinates(img, points=[4, 8, 12, 16, 20])
#     img = hd.draw_specific(img, [4, 8, 12, 16, 20])
#     # fps = hd.get_fps()
#     # img = cv.putText(img, f'FPS: {fps}', (10, 25), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
#     cv.imshow('Video', img)
#     cv.waitKey(1)
