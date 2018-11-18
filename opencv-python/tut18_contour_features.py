# python3 script using openCV
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html
# contour features

import cv2
import numpy as np

img = cv2.imread('opencv-logo2.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgGray, 50,255,0)

cv2.imshow('thresholded image',thresh)
cv2.waitKey(0)

bsImg, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# find the moments of the image
cont = contours[1]
M = cv2.moments(cont)
print(M)

# contour area and perimeter
area = cv2.contourArea(cont)
perimeter = cv2.arcLength(cont,True)
#			params(contour, true=closedContour, false=curve)

# contour approximations
''' if an object in an image is not idea (ex a skewed rectangle instead of square,
or rectangle with bites taken out)you can define an error term 'epsilon' to 
allow for an approximation of the desired shape
'''
epsilon = 0.1*cv2.arcLength(cont,True) # 10% of arc length allowable error
approx = cv2.approxPolyDP(cont, epsilon, True)
# approxPolyDP minimizes number of edges of an enclosing polygon about the given contour,
# while mainting a distance <=epsilon to the contour

# convex hulls
hull = cv2.convexHull(cont)
# params(points, orientation<clockwize>, returnPoints True returns hull points, false returns contour points on hull)

# checking convexity
k = cv2.isContourConvex(cont)

# bounding rectangle
x,y,width,height = cv2.boundingRect(cont)
cv2.rectangle(img,(x,y),(x+width,y+height),(0,255,0),2)
cv2.imshow('bounding rectangle',img)
cv2.waitKey(0)

# bounding rectangle that minimizes area by rotation
rect = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(rect)
box = np.int0(box) # convert to ints
cv2.drawContours(img,[box],0,(255,0,0), 1)
cv2.imshow('minimum bounding rectangle',img)
cv2.waitKey(0)

# bounding circles
(x,y),radius = cv2.minEnclosingCircle(contours[1])
center = (int(x),int(y))
radius = int(radius)
cv2.circle(img,center,radius,(255,255,0),2)
cv2.imshow('minimum bounding rectangle',img)
cv2.waitKey(0)

# fitting an ellipse NOT BOUNDING
ellipse = cv2.fitEllipse(contours[0])
cv2.ellipse(img, ellipse,(0,555,255),2)
cv2.imshow('approximate ellipse',img)
cv2.waitKey(0)

# fitting a line
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv2.fitLine(contours[1], cv2.DIST_L2,0,0.01,0.01)
# params(contours, distanceType, numericalParam,radialAccuracy, angularAccuracy)
# vx,vy are slope of infinite line. x,y is one point on line
lefty = int((cols-x)*vy/vx+y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(img,(cols-1,righty),(0,lefty),(100,150,200),2)
cv2.imshow('best fit line',img)
cv2.waitKey(0)


