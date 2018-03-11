# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_shi_tomasi/py_shi_tomasi.html
# shi-tomasi corner detector

import cv2
import numpy as np
from matplotlib import pyplot as plot

img = cv2.imread('blocks.jpg')
height, width = img.shape[:2]
img = cv2.resize(img, (int(width/2), int(height/2)), cv2.INTER_CUBIC)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,50,0.01,10)
# params(img, #corners, minCornerQuality, minDistBetweenCorners)
# minCorner quality is between 0 and 1

corners = np.int0(corners)

for i in corners:
	x,y = i.ravel()
	cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('shi-tomassi corners',img)
cv2.waitKey()
cv2.destroyAllWindows()