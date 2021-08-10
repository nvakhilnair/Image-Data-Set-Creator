from os import path
import cv2
import os
import numpy as np
import tensorflow as tf
import random

def zoom_in(files,path):
    count=1
    while(count <= (len(files)//4)):
        image=random.choice(files)
        img = cv2.imread(os.path.join(path,image))
        file_path = path + 'zoom_' + image
        img = tf.keras.preprocessing.image.random_zoom(
            img,(0.6,0.9), row_axis=0, col_axis=1, channel_axis=2
        )
        img=np.array(img)
        cv2.imwrite(file_path,img)
        count = count+1
