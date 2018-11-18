# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contour_properties/py_contour_properties.html
# contour properties

import cv2
import numpy as np

img = cv2.imread('opencv-logo2.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

bsImg, contours, hierarchy = cv2.findContours(imgGray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# aspect ratio of bounding box
x,y,width,height = cv2.boundingRect(contours[0])
aspectRatio = float(width)/height

# extent aka ratio of contour area to bounding box area
area = cv2.contourArea(contours[0])
rectArea = width*height
extent = float(area)/rectArea

# solidity aka ratio of contour area to convex hull area
hull = cv2.convexHull(contours[0])
hullArea = cv2.contourArea(hull)
solidity = float(area)/hullArea

# equivialent diameter aka diameter of cirlce with same area as contour area NOT bounding circle
eqDiam = np.sqrt(4*area/np.pi)

# orientation
(x,y), (majorAxis, minorAxis), angle = cv2.fitEllipse(contours[0])

# mask and pixels, aka the pixel coordinates of the object, returned in an x,y list
mask = np.zeros(imgGray.shape, np.uint8)
cv2.drawContours(mask,[contours[0]],0,255,-1)
pixelPoints = cv2.findNonZero(mask)

# max and min values
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(imgGray, mask = mask)

# extreme points in object
cont = contours[0]
leftMost = tuple(cont[cont[:,:,0].argmin()][0])
rightMost = tuple(cont[cont[:,:,0].argmax()][0])
topMost = tuple(cont[cont[:,:,1].argmin()][0])
bottomMost = tuple(cont[cont[:,:,1].argmax()][0])

