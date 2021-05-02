import cv2 as cv
import numpy as np

img = cv.imread('/home/arpitjain/Desktop/Code/Python/OpenCV/pictures/day.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)
#....laplacion
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
# cv.imshow('laplacion', lap)

#....Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

# cv.imshow('sobelx', sobelx)
# cv.imshow('sobely', sobely)
cv.imshow('combined sobel', combined_sobel)


cv.waitKey(0)