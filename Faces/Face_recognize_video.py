import cv2 as cv

video = cv.VideoCapture(0)
cascade_face = cv.CascadeClassifier('Python/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml')


while True:
    ret, frame = video.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    detections = cascade_face.detectMultiScale(frame_gray, 1.3, 5, minSize=(30,30))

    if(len(detections) > 0):
        (x,y,w,h) = detections[0]
        frame = cv.rectangle(frame, (x,y), (x+w,y+h), (255,255,0), thickness=3)
        print(f'number of faces detected = {len(detections)}')
    elif (len(detections) == 0):
        print('Number of faces detected = 0')   
    

    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
video.release()
cv.destroyAllWindows()
