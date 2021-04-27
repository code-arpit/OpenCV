import cv2 as cv

#....Reading images
img = cv.imread('/home/arpitjain/Desktop/PycharmProjects/opencv/pictures/falls.jpg')

cv.imshow('falls', img)

cv.waitKey(0)


#....Reading videos
# vid = cv.VideoCapture('/home/arpitjain/Desktop/PycharmProjects/opencv/videos/dog.mp4')
#
# while(True):
#     istrue, frame = vid.read()
#
#     cv.imshow('video', frame)
#
#     if cv.waitKey(20) & 0xFF==ord('q'):
#         break
#
# vid.release()
# cv.destroyAllWindows()
#


