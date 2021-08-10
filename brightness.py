import cv2
import os
import numpy as np
import tensorflow as tf
import random

def brightness_level(files,path):
    count=1
    while(count <= (len(files)//4)):
        image=random.choice(files)
        img = cv2.imread(os.path.join(path,image))
        increment=1
        while(increment<=2):
            file_path = path + 'brightness' + str(increment) + '_' + image
            img=tf.keras.preprocessing.image.random_brightness(
                img, (0.6,0.9)
                )
            img=np.array(img)
            cv2.imwrite(file_path,img)
            increment = increment + 1
        count = count+1
