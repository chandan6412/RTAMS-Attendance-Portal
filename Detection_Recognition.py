import sys
import cv2
import os
import tensorflow as tf, sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

faceCascade = cv2.CascadeClassifier("frontal_face.xml")
folder = "tf_face/face_photos/test_images"


# WHEN CLICK ON CLASSIFY THIS FUNCTION IS LOADED
def Detector():
    video_capture = cv2.VideoCapture(0)
    counter = 1
    while True:
        ret, frame = video_capture.read()
        FaceDetection(frame, counter)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        counter += 1
    video_capture.release()
    cv2.destroyAllWindows()

    print "Detection Completed"


#      *******************************************************************************************      #




# FACE DETECTION MODULE
def FaceDetection(frame, counter):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    # faces = normalize_faces(frame, faces)  # norm pipeline
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        imgCrop = frame[y:y + h, x:x + w]
        cv2.imshow('image croped', imgCrop)
        cv2.imwrite(folder + '/' + str(counter) + '.jpg', imgCrop)

    # Display the resulting frame
    # cv2.waitKey(1000)

    # cv2.imwrite(folder/nam +'/' + str(counter) + '.jpg', frame)
    cv2.imshow('Video', frame)


def createdataset(self):
    name = raw_input('Person: ').lower()
    folder = "tf_face/" + name  # input name
    if not os.path.exists(folder):
        os.mkdir(folder)
        n = True
    else:
        print "This name already exists"
        n = False

    if n:
        video_capture = cv2.VideoCapture(0)
        counter = 1
        while True:
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            # Draw a rectangle around the faces
            # faces = normalize_faces(frame, faces)  # norm pipeline
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                imgCrop = frame[y:y + h, x:x + w]
                cv2.imshow('image croped', imgCrop)
                cv2.imwrite(folder + '/' + str(counter) + '.jpg', imgCrop)

            # Display the resulting frame
            # cv2.waitKey(1000)

            # cv2.imwrite(folder/nam +'/' + str(counter) + '.jpg', frame)
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            counter += 1
        video_capture.release()
        cv2.destroyAllWindows()

        print "Detection Completed"


