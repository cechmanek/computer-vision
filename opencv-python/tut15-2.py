# python3 script using openCV
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_canny/py_canny.html
# canny edge detection - using slide bars to vary min and max edge thresholds

import cv2
import numpy as np

def nothing(x):
	pass
	#print(minThresh)

img = cv2.imread('robots.jpg',0)

cv2.namedWindow('myArea')

# create 3 trackbars
cv2.createTrackbar('min threshold', 'myArea', 0,500, nothing)
cv2.createTrackbar('max threshold', 'myArea', 500,1000, nothing)

while True:
	
	minThresh = cv2.getTrackbarPos('min threshold','myArea')
	maxThresh = cv2.getTrackbarPos('max threshold','myArea')
	edges = cv2.Canny(img, minThresh,maxThresh)
	# 		params(image, minEdgeGrad, maxEdgeGrad)
	cv2.imshow('original', img)
	
	cv2.imshow('myArea', edges)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
