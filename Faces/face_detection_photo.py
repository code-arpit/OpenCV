import cv2 as cv

img = cv.imread('/home/arpitjain/Desktop/Code/Python/OpenCV/pictures/me2.jpg')
image = cv.resize(img, (600,600))
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


cascade_face = cv.CascadeClassifier('/home/arpitjain/Desktop/Code/Python/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml')

faces_rect = cascade_face.detectMultiScale(gray, 1.2, 3)

print(f'number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(image, (x,y), (x+w,y+h), (0,255,0), thickness = 2)

cv.imshow('Detected faces', image)    




cv.waitKey(0)