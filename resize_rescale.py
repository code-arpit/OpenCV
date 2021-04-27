import cv2 as cv

#rescale (Used for images, videos , live video)
def rescaleFrame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
#....resize images

# img = cv.imread('/home/arpitjain/Desktop/PycharmProjects/opencv/pictures/falls.jpg')
#
# img_resized = rescaleFrame(img,0.2)
#
# cv.imshow('falls', img_resized)
#
# cv.waitKey(0)


#.....resize videos
# vid = cv.VideoCapture('/home/arpitjain/Desktop/PycharmProjects/opencv/videos/dog.mp4')
#
# while(True):
#     isTrue, frame = vid.read()
#
#     frame_resized =rescaleFrame(frame, 0.25)
#     cv.imshow('vid_resized', frame_resized)
#
#     if cv.waitKey(50) & 0xFF==ord('q'):
#         break
#
# vid.release()
# cv.destroyAllWindows()