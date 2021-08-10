import cv2
import sys
import os
def face_extract(output_Dir,scale_Factor,min_Neighbors,min_Size):
    files = os.listdir(output_Dir)
    for image in files:
        img = cv2.imread(os.path.join(output_Dir,image))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        try:
            faces = face_cascade.detectMultiScale(gray, scale_Factor,min_Neighbors,min_Size)
        except:
            faces = face_cascade.detectMultiScale(gray, 1.3,5,30)
        for (x, y, w, h) in faces:
            img = img[y:y+h, x:x+w]
        status = cv2.imwrite(os.path.join(output_Dir,image), img)
