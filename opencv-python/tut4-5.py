# python3 script using openCV
# drawing multiple objects via mouse

import numpy as np
import cv2

drawing = False # tracking to see when drawing is enabled
mode = True # true for rectange, false for circle

events = [i for i in dir(cv2) if 'EVENT' in i]

def draw_circle(event, x, y, flags, param):
	global ix, iy, drawing, mode
	
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y

	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing== True:
			if mode == True: # draw rectangle
				cv2.rectangle(img, (ix,iy),(x,y), (0,255,255), -1)
			else:
				cv2.circle(img, (x,y), 20, (255,255,0), -1)
	
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		if mode == True:
			cv2.rectangle(img, (ix,iy),(x,y), (0,255,255), -1)
		else:
			cv2.circle(img, (x,y), 20, (255,255,0), -1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('myCanvas')
cv2.setMouseCallback('myCanvas', draw_circle)

while True:
	cv2.imshow('myCanvas', img) # refresh display
	k = cv2.waitKey(1) & 0xFF
	if k == ord('m'): # press 'm' to switch modes
		mode = not mode
	elif k == 27:
		break

cv2.destroyAllWindows()

