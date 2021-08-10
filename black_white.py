import os
import cv2
def gray_scale(output_Dir):
    files = os.listdir(output_Dir)
    for image in files:
        img = cv2.imread(os.path.join(output_Dir,image))
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imwrite(os.path.join(output_Dir,image),img)
