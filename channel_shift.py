from os import path
import cv2
import os
import numpy as np
import tensorflow as tf
import random

def ch_shift(files,path):
    count=1
    while(count <= (len(files)//4)):
        image = random.choice(files)
        img = cv2.imread(os.path.join(path,image))
        file_path = path + 'channel_shift_' + image
        img = tf.keras.preprocessing.image.random_channel_shift(
        img,-50 , channel_axis=0
        )
        img=np.array(img)
        cv2.imwrite(file_path,img)
        count = count+1
