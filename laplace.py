import os
import cv2
def transform(output_Dir):
    files = os.listdir(output_Dir)
    for image in files:
        img = cv2.imread(os.path.join(output_Dir,image))
        img = cv2.Laplacian(img,cv2.CV_64F)
        img = img*2
        cv2.imwrite(os.path.join(output_Dir,image),img)