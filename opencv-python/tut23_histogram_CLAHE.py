# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html
# histograms -2: histogram equalization, contrast limited adaptive equalization (CLAHE)

import numpy as np
import cv2
from matplotlib import pyplot as plot

# equalization can be done in numpy or cv

img = cv2.imread('unequalized-hawkes.jpg',0)

height, width = img.shape

img = cv2.resize(img, None, fx = 1/2, fy = 1/2, interpolation = cv2.INTER_CUBIC)

#img = cv2.resize(img,img,[height/4,width/4],interpolation = CV_INTER_LINEAR)

clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8,8))
cl1 = clahe.apply(img)

result = np.hstack((img,cl1)) # stack images size by side

cv2.imshow('adaptive histogram equalization',result)
cv2.waitKey()