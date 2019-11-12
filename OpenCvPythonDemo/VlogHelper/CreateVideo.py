from cv2 import cv2
import numpy as np
import glob
import logging
 
img_array = []
for filename in glob.glob('/Users/albertsnow/Documents/Career/Cute/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (450,690)
    img = cv2.resize(img, size)
    # cv2.imshow("Show by CV2", img)
    # cv2.waitKey(0)

    img_array.append(img)
    logging.error('%s fileName, %f height, %f width', filename, height, width)

 
out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()