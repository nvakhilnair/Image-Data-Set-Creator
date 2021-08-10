import os
from os import path
import cv2
def image_resize(path,width,height):
    files = os.listdir(path)
    for image in files:
        img = cv2.imread(os.path.join(path,image))
        try:
            img = cv2.resize(img, (width,height))
        except:
            img = cv2.resize(img, (200,200))
        cv2.imwrite(os.path.join(path,image),img)