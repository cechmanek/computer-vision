# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
# template matching

import cv2
import numpy as np
from matplotlib import pyplot as plot

searchImage = cv2.imread('Messi.png')
searchImage = cv2.cvtColor(searchImage, cv2.COLOR_RGB2BGR)
img2 = searchImage.copy()

target = cv2.imread('Messi-head.png')

height, width = target.shape[:2]

# list comparison methods
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR',
		   'cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for m in methods:
	img = img2.copy() 
	method = eval(m)
	
	# apply template matching
	res = cv2.matchTemplate(img, target, method)
	minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
	
	# if method is TM_SQDIFF or TM_SQDIFF_NORMED take min instead of max
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		topLeft = minLoc # top left corner of matched area
	else:
		topLeft = maxLoc
	
	bottomRight = (topLeft[0] + width, topLeft[1] + height)
	
	cv2.rectangle(img, topLeft, bottomRight, 255, 2) # draw a box around matched area
	
	plot.subplot(121), plot.imshow(res,cmap = 'gray')
	plot.title('Matching Result'), plot.xticks([]), plot.yticks([])
	plot.subplot(122), plot.imshow(img,cmap = 'gray')
	plot.title('Detected Point'), plot.xticks([]), plot.yticks([])
	plot.suptitle(m)

	plot.show()
	
	