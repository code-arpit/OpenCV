import cv2 as cv

img = cv.imread('/home/arpitjain/Desktop/Code/Python/OpenCV/pictures/day.jpg')
image = cv.resize(img, (700,500), interpolation = cv.INTER_AREA)
# cv.imshow('image', image)

#....Averaging(average of surrounding pixels)
average = cv.blur(image, (7,7))
# cv.imshow('average', average)

#....Gaussian_blur(more real than average)
gauss = cv.GaussianBlur(image, (7,7), 0)
# cv.imshow('gausss', gauss)

#....Median_blur(median of surrounding pixels
median = cv.medianBlur(image, 3)
cv.imshow('median', median)

#....bilateral_blurring
bilateral = cv.bilateralFilter(image, 10, 35, 25)
cv.imshow('nilateral', bilateral)

cv.waitKey(0)