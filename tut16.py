# python3 script using openCV
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_pyramids/py_pyramids.html
# image pyramids
# image blending example. error with pyramid images not being the same size

import cv2
import numpy as np

# load images
apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')

#create gaussian pyramdids
gausApple = apple.copy()
gausApplePyr = [gausApple]
gausOrange = orange.copy()
gausOrangePyr = [gausOrange]

for i in range(6):
	gausApple = cv2.pyrDown(gausApple)
	gausApplePyr.append(gausApple)
	
	gausOrange = cv2.pyrDown(gausOrange)
	gausOrangePyr.append(gausOrange)

# create laplacians from image pyramids
lapApple = [gausApplePyr[5]]
lapOrange = [gausOrangePyr[5]]
for i in range(5,0,-1):
	GE = cv2.pyrUp(gausApplePyr[i])
	print(gausApplePyr[i-1].shape)
	print(GE.shape)
	L = cv2.subtract(gausApplePyr[i-1], GE)
	lapApple.append(L)
	
	GE2 = cv2.pyrUp(gausOrangePy[i])
	L2 = cv2.subtract(gausOrangePyr[i-1], GE2)
	lapOrange.append(L2)

# add halves of images together
LS = [] # list of paired images
for la, lb in zip(lapApple,LapOrange):
	rows,cols, depth = la.shape
	ls = np.hstack((la[:,0,cols/2], lb[:,cols/2:])) # horizontally stack the image arays
	LS.append(ls)

# rebuild the image from the pyramids
blend = LS[0]
for i in range(1,6):
	blend = cv2.pyrUp(blend)
	blend = cv2.add(blend,LS[i])

# compare to simple merge
simple = np.hstack((Apple[:,:,cols/2], Orange[:,cols/2,:]))

cv2.imshow('simple merge', simple)
cv2.imshow('pyramid blend', blend)
			
				   