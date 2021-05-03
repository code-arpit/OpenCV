import os 
import cv2 as cv
import numpy as np

people = []
for i in os.listdir(r'/home/arpitjain/Desktop/Code/Python/OpenCV/pictures'):
        people.append(i)

print(people)

DIR = r'/home/arpitjain/Desktop/Code/Python/OpenCV/pictures'

cascade_face = cv.CascadeClassifier('/home/arpitjain/Desktop/Code/Python/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml')

features = []
labels = []
def create_train():
    for person in people:
        path = os.path.join(DIR, person)   
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = cascade_face.detectMultiScale(gray, 1.2, 5)
            for (x,w,y,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

print(f'length of features list = {len(features)}')
print(f'length of labels list = {len(labels)}')
