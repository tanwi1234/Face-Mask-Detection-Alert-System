
import cv2
import os
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image=cv2.imread("with_mask606.jpeg")
images=cv2.resize(image, (500, 300))
gray=cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray,1.1,4)
for (x, y, w, h) in faces:
    cv2.rectangle(images, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("img",images)
cv2.waitKey()





