from os import path
import cv2
import os
import numpy as np
import tensorflow as tf
import random

def rotate(files,path):
    count=1
    while(count <= (len(files)//4)):
        image=random.choice(files)
        img = cv2.imread(os.path.join(path,image))
        for angle  in range(30,90,30):
            file_path = path + 'rotate_' + str(angle) + '_' + image
            img = tf.keras.preprocessing.image.random_rotation(
                img,
                30,
                row_axis=0,
                col_axis=1,
                channel_axis=2
            )
            img=np.array(img)
            cv2.imwrite(file_path,img)
        count = count+1