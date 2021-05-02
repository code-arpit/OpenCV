import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('/home/arpitjain/Desktop/Code/Python/OpenCV/pictures/day.jpg')
# cv.imshow('image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray image', gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 150, 255, -1)
# cv.imshow('circle', circle)

mask_gray = cv.bitwise_and(gray, gray, mask=mask)
# cv.imshow('masked gray scale image', mask_gray)
mask_color = cv.bitwise_and(img, img, mask=mask)
# cv.imshow('masked gray scale image', mask_color)

#....Grayscale histogram
# gray_hist = cv.calcHist([gray], [0], mask_gray, [256], [0,256])

# plt.figure()
# plt.title('grayscale histogram')
# plt.xlabel('Bins')
# plt.ylabel('no. of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()
    
#....Coloured histogram
plt.figure()
plt.title('Coloured Histogram')
plt.xlabel('Bins')
plt.ylabel('no. of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    color_hist = cv.calcHist([img], [i], mask=mask, histSize=[256], ranges=[0,256])
    plt.plot(color_hist, color=col)
    plt.xlim([0,256])

plt.show()    
 

cv.waitKey(0)
