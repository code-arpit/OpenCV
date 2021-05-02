import cv2 as cv

img = cv.imread('/home/arpitjain/Desktop/Code/Python/OpenCV/pictures/me3.jpg')
image = cv.resize(img, (600,600))
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


haar_cascade = cv.CascadeClassifier('/home/arpitjain/Desktop/Code/Python/OpenCV/Faces/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, 1.5, 3)

print(f'number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(image, (x,y), (x+w,y+h), (0,255,0), thickness = 2)

cv.imshow('Detected faces', image)    




cv.waitKey(0)