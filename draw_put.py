import cv2 as cv
import numpy as np
from numpy import ndarray

blank= np.zeros((400, 600, 3), dtype='uint8')
cv.imshow('New Blank Window', blank)

# ....paint the image
#blank[0:200, 0:200] = 0, 255, 0
#cv.imshow('coloured window', blank)

# ....rectangle
# cv.rectangle(blank, (0,0), (200,400), (0,0,255), thickness=-1)
# cv.rectangle(blank, (200,200), (600,400), (0,255,0), thickness=-1)
# cv.imshow('rectangle inside window', blank)

#....circle
# cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 50, (0,255,0), thickness=-1 )
# cv.imshow('circle in blank', blank)

#....line
# cv.line(blank, (0,0), (250,250), (0,255,0))
# cv.imshow('line in blank', blank)

#....text on image
# cv.putText(blank, 'hello World',(200,200), cv.FONT_ITALIC, 2.0, (0,255,0), 2)
# cv.imshow('text on image', blank)

cv.waitKey(0)