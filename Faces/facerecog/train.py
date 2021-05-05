import os
from PIL import Image
import numpy as np
import cv2 as cv
import pickle
#..name of current file ->
Base_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(Base_dir, "pictures")

cascade_face = cv.CascadeClassifier('/home/arpitjain/Desktop/Code/Python/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
recognizer = cv.face.LBPHFaceRecognizer_create()


current_id = 0
label_id = {}
y_labels = [] # contains label indexes
x_train = [] # contains image data as numpy array

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("jpg") or file.endswith("jpeg"):
            paths = os.path.join(root, file)
            labels = os.path.basename(os.path.dirname(paths)).lower()
            # print(labels, paths)
            
            if labels in label_id:
                pass
            else:
                label_id[labels] = current_id
                current_id += 1
                
            id_ = label_id[labels]
            # print(label_id)
            # y_labels.append(labels) # some number 
            # x_train.append(paths)  # verify this image, turn into numpy array, turn into gray
            pil_image = Image.open(paths).convert("L") #..grayscale
            image_array = np.array(pil_image, dtype='uint8')
            # print(image_array)
            faces = cascade_face.detectMultiScale(image_array, 1.2, 5)

            for (x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

# print(y_labels)
# print(x_train)                

# with open("labels.pickle", 'wb') as f:
#     pickle.dump(label_id, f)

# recognizer.train(x_train, np.array(y_labels))
# recognizer.save("trainer.yml")
