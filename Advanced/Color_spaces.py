import cv2 as cv 

img = cv.imread('/home/arpitjain/Desktop/Code/Python/OpenCV/pictures/falls.jpg')
image = cv.resize(img, (700,500),interpolation=cv.INTER_AREA)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

cv.waitKey(0)