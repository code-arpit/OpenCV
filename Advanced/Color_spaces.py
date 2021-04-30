import cv2 as cv 

img = cv.imread('/home/arpitjain/Desktop/Code/Python/OpenCV/pictures/falls.jpg')
image = cv.resize(img, (700,500),interpolation=cv.INTER_AREA)
# cv.imshow('image', image)

#....BGR to Grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

#....BGR to HSV
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
# cv.imshow('hsv', hsv)

#....BGR to L*a*b
lab = cv.cvtColor(image, cv.COLOR_BGR2LAB)
# cv.imshow('lab', lab)

rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)



cv.waitKey(0)