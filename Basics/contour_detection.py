import cv2 as cv 
import numpy as np

img = cv.imread('/home/arpitjain/Desktop/Code/Python/OpenCV/pictures/falls.jpg')
image = cv.resize(img, (700,500), interpolation=cv.INTER_AREA)


blank= np.zeros((500, 700, 3), dtype='uint8')


gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)


blurr = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)

canny = cv.Canny(blurr, 125, 175)
cv.imshow('canny', canny)

contours, heirarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours')

cv.drawContours(blank, contours, -1, (0,0,255))
cv.imshow('contours drawn', blank)





cv.waitKey(0)