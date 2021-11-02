# python3 script using opencv
#image thresholding
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html


import cv2
import numpy as np
from matplotlib import pyplot as plot

# load image as grayscale
img = cv2.imread('robots.jpg',0)

ret, threshImg1 = cv2.threshold(img,127,255, cv2.THRESH_BINARY)
ret, threshImg2 = cv2.threshold(img,127,255, cv2.THRESH_BINARY_INV)
ret, threshImg3 = cv2.threshold(img,127,255, cv2.THRESH_TRUNC)
ret, threshImg4 = cv2.threshold(img,127,255, cv2.THRESH_TOZERO)
ret, threshImg5 = cv2.threshold(img,127,255, cv2.THRESH_TOZERO_INV)
#					params(image, bounds, threshold type)

titles = ['original', 'binary', 'binary inverse', 'truncated', 'to zero', 'to zero inverse']
images = [img, threshImg1, threshImg2, threshImg3, threshImg4, threshImg5]

for i in range(6):
	plot.subplot(2,3,i+1)
	plot.imshow(images[i],'gray')
	
	plot.title(titles[i])
	plot.xticks([])
	plot.yticks([])
	
plot.show()