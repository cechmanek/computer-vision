# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
# Hough line transform


import cv2
import numpy as np

img = cv2.imread('sudoku.jpg',0)
height, width = img.shape[:2]

img = cv2.resize(img, (int(height/3), int(width/3)), interpolation = cv2.INTER_CUBIC) 
original = img.copy()

edges = cv2.Canny(img, 50, 150, apertureSize = 3)
# NOTE: edge detection is impacted by image size

lines = cv2.HoughLines(edges, 1, np.pi/180, 140)
#			params(edges, rho, theta, threshold)
# rho is min line length
# theta is range of angles 

print(lines.shape)
#print(lines)
count = 0

for rho, theta, in lines[:,0,0:]:
	#print(rho, theta)
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a*rho
	y0 = b*rho
	x1 = int(x0 +1000*(-b))
	y1 = int(y0 +1000*(a))
	x2 = int(x0 -1000*(-b))
	y2 = int(y0 -1000*(a))
	
	#print('counter: ',count)
	count += 1
	print(x1,x2,y1,y2)
	cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

testing = np.mat(img) - np.mat(original)

combine = np.hstack((original,img))

cv2.imshow(' Hough lines result', combine)
cv2.waitKey()
cv2.destroyAllWindows()