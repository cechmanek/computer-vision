# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html
# Hough circle transform

import cv2
import numpy as np

img = cv2.imread('opencv-logo2.png',0)

img = cv2.medianBlur(img,5)
colorImg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1,20, param1 = 50, param2 = 20
					   , minRadius = 0, maxRadius = 0)
# params(img, detection method, acumulator relative size 1=same as image, 2=half width & height,
# min distance between circle centers, param1=?? , raise param2 for less false positives,
# currently the only method is cv2.HOUGH_GRADIENT
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
	# draw out circle
	cv2.circle(colorImg, (i[0],i[1]),i[2], (0,255,0),2)
	
	# draw cirlce center
	cv2.circle(colorImg, (i[0], i[1]), 2, (255,0,0), 2)
	
cv2.imshow('found cirlces', colorImg)
cv2.waitKey()
cv2.destroyAllWindows()
