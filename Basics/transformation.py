import cv2 as cv
import numpy as np

img = cv.imread('/home/arpitjain/Desktop/Code/Python/OpenCV/pictures/falls.jpg')
image = cv.resize(img, (700, 500), interpolation=cv.INTER_AREA)


# ...translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], image.shape[0])

    return cv.warpAffine(img, transMat, dimensions)


# ....rotation
def rotate(img, angle, rotpoint=0):
    (height, width) = img.shape[0:2]

    if rotpoint == 0:
        rotpoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


# +x --> move right
# -x --> move left
# +y --> move down
# -y --> move up
# translated_image = translate(image, -100, -100)
# cv.imshow('translated image', translated_image)


# -angle --> clockwise rotation
# +angle --> anticlockwise rotation
# rotate_image = rotate(image, -45)
# cv.imshow('rotated image', rotate_image)

# #.... Flipping
# flip = cv.flip(image, -1)
flip = cv.flip(image, -1)
# cv.imshow('flipped image', flip)

# #....cropping
cropped = image[100:200,200:400]
# cv.imshow('cropped', cropped)

cv.waitKey(0)
