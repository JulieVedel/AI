import cv2

data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('Angelina.jpg')

grayscaledImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCoordinates = data.detectMultiScale(grayscaledImage)

for (x, y, w, h) in faceCoordinates:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)



cv2.imshow('Program', image)
cv2.waitKey()


