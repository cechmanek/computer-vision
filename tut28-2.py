# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
# Hough line transform - probabalistic detection
import cv2
import numpy as np

img = cv2.imread('sudoku.jpg')
height, width = img.shape[:2]

img = cv2.resize(img, (int(height/3), int(width/3)), interpolation = cv2.INTER_CUBIC) 
original = img.copy()

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)

print(lines.shape)

for x1,y1,x2,y2 in lines[:,0,0:]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

combine = np.hstack((original, img))
	
cv2.imshow('probabalistic hough lines',combine)
cv2.waitKey()
cv2.destroyAllWindows()