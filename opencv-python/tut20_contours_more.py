# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contours_more_functions/py_contours_more_functions.html
# contours: more functions

import cv2
import numpy as np

img = cv2.imread('fourPointStar.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgGray, 50,255,0)

bsImg, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont1 = contours[0]
cont2 = contours[1]

#convexity defects
hull = cv2.convexHull(cont1, returnPoints = False)
defects = cv2.convexityDefects(cont1,hull)
# defects is an array with each point :
# [ start point, end point, farthest point, approximate distance to farthest point ]

for i in range(defects.shape[0]):
	s,e,f,d = defects[i,0]
	# start, end, farthest, distance
	
	start = tuple(cont1[s][0])
	end = tuple(cont1[e][0])
	farthest = tuple(cont1[f][0])
	cv2.line(img,start,end,[0,255,255],1)# incrementally draws lines between convex hull points
	cv2.circle(img,farthest,5,[255,255,0],3,-1)# circles farthest points from convex hull
	
cv2.imshow('image with convexities',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# point polygon test
# find the min distance between a point an a polygon, negative distances mean point is outside polygon 
dist = cv2.pointPolygonTest(cont1,(50,50),True)
#		params(contour,point, True returns signed distance, False returns -1 or 1 for inside or outside
print("distance between point and contour:")
print(dist)

# matching shapes
img1 = cv2.imread('fourPointStar.png',0)
img2 = cv2.imread('fourPointStar2.png',0)
#img2 = cv2.imread('opencv-logo2.png',0)

ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 130, 255,0)
cv2.imshow('img1',thresh)
cv2.imshow('img2',thresh2)
cv2.waitKey(0)

bsImg,contours1,hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours1[0]
bsImg,contours2,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours2[0]

ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print('degree of match between fourpointstar and fourpointstar2: ')
print(ret)

