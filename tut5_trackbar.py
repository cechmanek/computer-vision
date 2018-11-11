# python3 script using openCV
# create a trackbar to choose color

import numpy as np
import cv2

def nothing(x):
	pass
	
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('myArea')

# create 3 trackbars
cv2.createTrackbar('R', 'myArea', 0,255, nothing)
cv2.createTrackbar('G', 'myArea', 0,255, nothing)
cv2.createTrackbar('B', 'myArea', 0,255, nothing)
#params(barName, displayArea, range, onChangeFunction)

# create on/off switch
switch = '0 :OFF\n1 : ON'
cv2.createTrackbar(switch, 'myArea', 0, 1, nothing)

while True:
	cv2.imshow('myArea', img)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
	
	r = cv2.getTrackbarPos('R', 'myArea')
	g = cv2.getTrackbarPos('G', 'myArea')
	b = cv2.getTrackbarPos('B', 'myArea')
	s = cv2.getTrackbarPos(switch, 'myArea')
	
	if s == 0:
		img[:] = 0 # set image blank
	else:
		img[:] = [b,g,r]