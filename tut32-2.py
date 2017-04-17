# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html
# Harris corner detection

'''
cv2.cornerHarris()

params(img, blocksize, ksize, k)
img - Input image, it should be grayscale and float32 type.
blockSize - It is the size of neighbourhood considered for corner detection
ksize - Aperture parameter of Sobel derivative used.
k - Harris detector free parameter in the equation.

cv2.cornerSubPix()
'''

import cv2
import numpy as np

def nothing(x):
	pass

def changeBlock(x):
	print('new block size: ',blockSize)

def changeKsize(x):
	print('new k size: ',kSize)

def changeK(x):
	print('new k: ',k)

img = cv2.imread('blocks.jpg')
height, width = img.shape[:2]
img = cv2.resize(img, (int(width/2), int(height/2)), cv2.INTER_CUBIC)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

cv2.namedWindow('myArea')

# create 3 trackbars
cv2.createTrackbar('block size', 'myArea', 1,25, changeBlock)
cv2.createTrackbar('k size', 'myArea', 1,25, changeKsize)
cv2.createTrackbar('k parameter', 'myArea', 1,10, changeK)
oldk = 0
while True:
	
	blockSize = cv2.getTrackbarPos('block size','myArea')
	blockSize = max([blockSize, 1])
	kSize = cv2.getTrackbarPos('ksize','myArea')
	kSize = max([kSize,1])
	k = cv2.getTrackbarPos('k parameter','myArea')
	
	dst = cv2.cornerHarris(gray,blockSize,kSize,k/100)

	#result is dilated for marking the corners, not important
	dst = cv2.dilate(dst,None)

	# Threshold for an optimal value, it may vary depending on the image.
	
	display = img.copy() # don't change original
	display[dst>0.01*dst.max()]=[0,0,255]
	
	cv2.imshow('myArea',display)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
