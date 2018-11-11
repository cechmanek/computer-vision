# python3 script using openCV
# painting with mouse pointer

import cv2
import numpy as np

#list all possible mouse events (lclick, rclick, doubleclick, etc)
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def draw_circle(event, x,y,flags, param):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img,(x,y), 100,(255,0,0),-1)
		
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('myCanvas')

#link function of mouse callback event, params get passed automatically 
cv2.setMouseCallback('myCanvas', draw_circle)

while (True):
	cv2.imshow('myCanvas', img)
	if cv2.waitKey(20) & 0xFf ==27: # if exc pressed
		break

cv2.destroyAllWindows()