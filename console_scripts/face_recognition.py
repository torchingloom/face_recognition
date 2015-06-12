# coding: utf-8
import os
import cv2
import sys

def main():
    try:
        img_path = os.path.abspath(sys.argv[1])
        image = cv2.imread(img_path)
    except:
        print 'Bad image path'
        exit()

    casc_path = os.path.join('static', 'haarcascade_frontalface_default.xml')
    if len(sys.argv) > 2:
        casc_path = sys.argv[2]
    if not os.path.exists(casc_path):
        print 'Bad haarcascade frontalface xml'
        exit()

    # Create the haar cascade
    face_cascade = cv2.CascadeClassifier(casc_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print "Found {0} faces!".format(len(faces))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces found", image)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
