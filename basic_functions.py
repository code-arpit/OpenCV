import cv2 as cv


def rescale_frame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('/home/arpitjain/Desktop/PycharmProjects/opencv/pictures/falls.jpg')

#....rescale
# img_rescale = rescale_frame(img, 0.25)
# cv.imshow('falls', img_rescale)

#....converting to grayscale
# gray = cv.cvtColor(img_rescale, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

#....BLur
# blur = cv.GaussianBlur(img_rescale, (9,9), cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

#....edge cascade
# canny = cv.Canny(img_rescale, 175, 175)
# cv.imshow('canny',canny)

#....dilating image
# dilated = cv.dilate(canny, (3,3), iterations=9)
#cv.imshow('dilates', dilated)

#....eroding
# eroded = cv.erode(canny, (3,3), iterations=3)
# cv.imshow('eroded', eroded)

#....resize
# resized = cv.resize(img_rescale, (500,300), interpolation=cv.INTER_AREA)
# cv.imshow('resized', resized)

#....cropping
# cropped = img_rescale[0:100,100:200]
# cv.imshow('cropped', cropped)



cv.waitKey(0)
