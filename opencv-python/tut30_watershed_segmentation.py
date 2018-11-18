# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_watershed/py_watershed.html
# image segmentation with watershed algorithm

import cv2
import numpy as np

img = cv2.imread('watershed-coins.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#cv2.imshow('thresholded coins',thresh)
#cv2.waitKey()

# because coins are touching use erosion and dilation to remove noise
# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# identify area we are sure is background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)

# identify area we are sure is foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

myStack = np.hstack((dist_transform,sure_fg,sure_bg,unknown))

cv2.imshow('threshold, foreground, background(in black), unkown',myStack)
cv2.waitKey()

# now combine foregound and background
# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]

# final result
cv2.imshow('watershed',img)
cv2.waitKey()
