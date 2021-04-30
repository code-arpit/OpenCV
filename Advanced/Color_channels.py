import cv2 as cv 
import numpy as np

img = cv.imread('/home/arpitjain/Desktop/Code/Python/OpenCV/pictures/falls.jpg')
image = cv.resize(img, (700,500),interpolation=cv.INTER_AREA)
cv.imshow('image', image)

b,g,r = cv.split(image)

cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

print(image.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)

blank = np.zeros(image.shape[0:2], dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

cv.waitKey