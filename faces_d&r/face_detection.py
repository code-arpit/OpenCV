import cv2 as cv

img = cv.imread('/home/arpitjain/Desktop/Code/Python/OpenCV/pictures/me2.jpg')
image = cv.resize(img, (600,700))
cv.imshow('me', image)

cv.waitKey(0)