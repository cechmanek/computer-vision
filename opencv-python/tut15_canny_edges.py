# python3 script using openCV
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_canny/py_canny.html
# canny edge detection

import cv2
import numpy as np
from matplotlib import pyplot as plot

img = cv2.imread('robots.jpg',0)

edges = cv2.Canny(img, 100,200)
# 		params(image, minEdgeGrad, maxEdgeGrad)

plot.subplot(1,2,1), plot.imshow(img, cmap = 'gray')
plot.title('original')
plot.subplot(1,2,2), plot.imshow(edges, cmap = 'gray')
plot.title('canny edges')

plot.show()
