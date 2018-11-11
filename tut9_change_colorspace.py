# python3 script using openCV
''' left off here:
http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html
'''
# changing colorspaces

import cv2
import numpy as np

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

# note: HSV values range from [0-179,0.255,0.255] in opencv

# create a tracker for blue objects
cap = cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()
	
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	# define blue range in hsv
	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])
	lower_green = np.array([50,50,50])
	upper_green = np.array([70,255,255])
	
	# threshold hsv frame to get only blue
	blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
	green_mask = cv2.inRange(hsv, lower_green, upper_green)
	
	#bitwise AND mask the frame
	blue_result = cv2.bitwise_and(frame, frame, mask = blue_mask)
	green_result = cv2.bitwise_and(frame, frame, mask = green_mask)
	#                 params(image1, image2, mask=mask)
	# img 1 and 2 get ANDED, then masked
	
	cv2.imshow('frame', frame)
	cv2.imshow('mask', blue_mask)
	
	cv2.imshow('blue result', blue_result)
	cv2.imshow('green result', green_result)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()

# to find hsv values that corespond to bgr you can do:
green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)
# prints out: [[[ 60 255 255]]]