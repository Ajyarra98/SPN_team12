import os
import pickle

import mediapipe as mp
import cv2
import matplotlib.pyplot as plt


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = './rawdata'

data = []
labels = []
def multilandmarks(results):
    x_ = []
    y_ = []
    data_list = []
    for hand_landmarks in results.multi_hand_landmarks:
        i=0
        while(i < len(hand_landmarks.landmark)):
            x = hand_landmarks.landmark[i].x
            y = hand_landmarks.landmark[i].y
            x_.append(x)
            y_.append(y)
            i=i+1

        ## Normalization of landmarks
        i=0
        while(i<len(hand_landmarks.landmark)):
            x = hand_landmarks.landmark[i].x
            y = hand_landmarks.landmark[i].y
            data_list.append(x - min(x_))
            data_list.append(y - min(y_))
            i=i+1
    return data_list
    
for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        data_list = []

        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            data_list = multilandmarks(results)

            data.append(data_list)
            labels.append(dir_)

f = open('dataset.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()
