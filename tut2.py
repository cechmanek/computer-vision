# Python3 script using openCV
# video capture

import numpy as np
import cv2
from matplotlib import pyplot as plot

cap = cv2.VideoCapture(0)

if not cap.isOpened():
	print("didn't get camera")

while (cap.isOpened()):
	#capture frame by frame
	ret, frame = cap.read()
	
	#do some operations on frame
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# dsiplay
	cv2.imshow('myFrame', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# release camera
cap.release()
cv2.destroyAllWindows()

# play vid from file

cap = cv2.VideoCapture('bike.mpg')
if not cap.isOpened():
	print("didn't load video")

while cap.isOpened():
	ret, frame = cap.read()
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	cv2.imshow('myframe', gray)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
	   break

# release video
cap.release()
cv2.destroyAllWindows()