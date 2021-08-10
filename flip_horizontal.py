from os import path
import cv2
import os
import numpy as np
import tensorflow as tf
import random

def flip(files,path):
    count=1
    while(count <= (len(files)//4)):
        image=random.choice(files)
        file_path = path + 'fliped' + image
        img = cv2.imread(os.path.join(path,image))
        img = tf.image.flip_left_right(img)
        img=np.array(img)
        cv2.imwrite(file_path,img)
        count = count+1