# python3 script using openCV
# timing functions to evaluate performance

import cv2

img1 = cv2.imread('robots.jpg')

e1 = cv2.getTickCount()
## code being timed, median filtering with filter size from 5 to 49
for i in range(5,49,2):
	img1 = cv2.medianBlur(img1,i)
##
e2 = cv2.getTickCount()

seconds = (e2 - e1)/cv2.getTickFrequency()
print(seconds)