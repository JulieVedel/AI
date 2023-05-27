import cv2

data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam = cv2.VideoCapture(0)

while True:
    success, frame = webcam.read()
    grayscaledFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faceCoordinates = data.detectMultiScale(grayscaledFrame)

    for (x, y, w, h) in faceCoordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Program', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break
    
webcam.release()



