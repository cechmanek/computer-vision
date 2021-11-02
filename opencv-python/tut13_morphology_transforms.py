# python3 script using opencV
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html
# morphological transformations

import cv2
import numpy as np
from matplotlib import pyplot as plot

img = cv2.imread('j.png',0)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)

dilation = cv2.dilate(img,kernel, iterations = 1)

# opening. equivalent to erosion then dilation of equal amount. remoives noise
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# closing. equivalent to dilation then erosion of equal amount. fills holes in objects
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# morphology gradient. difference between dilation and erosion
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# tophat. difference between input image and opening
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# blackhat. difference between closing and input image
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

plot.subplot(241),plot.imshow(img),plot.title('original')
plot.subplot(242),plot.imshow(erosion),plot.title('erosion')
plot.subplot(243),plot.imshow(dilation),plot.title('dilation')
plot.subplot(244),plot.imshow(opening),plot.title('opening')
plot.subplot(245),plot.imshow(closing),plot.title('closing')
plot.subplot(246),plot.imshow(gradient),plot.title('gradient')
plot.subplot(247),plot.imshow(tophat),plot.title('top hat')
plot.subplot(248),plot.imshow(blackhat),plot.title('black hat')

plot.show()

