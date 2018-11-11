# python3 script using openCV
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.html#contours-getting-started
# contours: getting started

import cv2
import numpy as np

img = cv2.imread('opencv-logo2.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgGray, 50,255,0)

cv2.imshow('thresholded image',thresh)
cv2.waitKey(0)

bsImg, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#						params(image, contour retrieval mode, contour approx method)
# 'contours' is a a list of arrays, each individual array is an array of one contour

# drawing all contours
newImg = cv2.drawContours(img, contours, -1, (255,0,255), 3)
#		params(image, listOfArrays,which contours to draw -1=all , color, thickness)

# drawing one contour
myFavContour = contours[0]
newImg2 = cv2.drawContours(img, myFavContour,-1, (255,0,255), 3)

cv2.imshow('image with contours',img)
cv2.imshow('my new image',newImg)
cv2.waitKey(0)