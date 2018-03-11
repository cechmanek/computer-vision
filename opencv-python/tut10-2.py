# python3 script using opencv
#image thresholding - adaptive thresholding
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html

import cv2
import numpy as np
from matplotlib import pyplot as plot

# load image as grayscale
img = cv2.imread('threshold.jpg',0)

ret, threshImg1 = cv2.threshold(img,127,255, cv2.THRESH_BINARY)

threshImg2 = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C,\
								   cv2.THRESH_BINARY, 11,2)
threshImg3 = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
							   cv2.THRESH_BINARY,11,2)
#params(image, maxValue, adaptiveMethod, thresholdType, blockSize, constantAdjustment)

titles = ['original', 'binary', 'adaptive mean C', 'adaptive Gaussian']
images = [img, threshImg1, threshImg2, threshImg3]

for i in range(4):
	plot.subplot(2,2,i+1)
	plot.imshow(images[i],'gray')
	
	plot.title(titles[i])
	plot.xticks([])
	plot.yticks([])
	
plot.show()