# python3 script using opnecv
# drawing tools

import numpy as np
import cv2

# initialize empy image
img = np.zeros((512,512,3), np.uint8)

# draw diagonal line
cv2.line(img,(0,0), (511,511), (255,0,0), 5)
# params(image, start, end, color, linetype)

cv2.rectangle(img, (380,0),(510,120), (0,255,0), 3)
#params(image, firstcorner, second corner, color, linetype)


cv2.circle(img, (150, 100), 55, (0,0,255), -1)
#params(image, center, radius, color, -1=fill)

cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#center, majorAxis, minorAxis, angle, startAngle, endAngle, color, linetype

# define corners of polygon
points = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
print(points)
print("")
points = points.reshape((-1,1,2))
print(points)
cv2.polylines(img, [points], True, (0,255,255),3)
#params(image,corners,True=closed polygon, color, linetype)

#writing text to an image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV',(10,500), font, 4,(25,250,255),2, cv2.LINE_AA)
#params(image, text,position, fontType, fontSize, color, thickness, linetype)


cv2.imshow('myimage',img)
cv2.waitKey(0)
cv2.destroyAllWindows()