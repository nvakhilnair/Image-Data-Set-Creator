import cv2
import os
import numpy as np
import tensorflow as tf
import random

def shift(files,path):
    count=1
    while(count <= (len(files)//4)):
        image=random.choice(files)
        img = cv2.imread(os.path.join(path,image))
        for shift  in range(2,10,2):
            file_path = path + 'shift_' + str(shift) + '_' + image
            img = tf.keras.preprocessing.image.random_shift(
                img,0.2, 0.2, row_axis=0, col_axis=1, channel_axis=2
            )
            img=np.array(img)
            cv2.imwrite(file_path,img)
        count = count+1