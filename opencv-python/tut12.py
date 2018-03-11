# python3 script using openCV
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_filtering/py_filtering.html
# smoothing images

import cv2
import numpy as np
from matplotlib import pyplot as plot

img = cv2.imread('opencv-logo2.png')

kernel = np.ones((5,5), np.float32)/25 # 5x5 flat filter
result = cv2.filter2D(img, -1, kernel)
# params(image, depth, filter) if depth=-1 then result depth = image depth

# OR
result = cv2.blur(img,(5,5)) # this assumes a normalized flat filter

# gaussian bluring
gaussBlur = cv2.GaussianBlur(img,(5,5),0)
#			params(img, filterSize, stdevX, stdevY)
# if only stdevX given stdevY=stdevX, if 0 then stdevX,Y calculated from image

# median blurring
medBlur = cv2.medianBlur(img, 5)
# median filter assumed square, should be odd value

# bilateral filter. 
''' standard gaussian is only a function of location in image,
bilateral filter combines this with another term that accounts for image intensity
goal is to not filter across edges
'''
bilatBlur = cv2.bilateralFilter(img,9,75,75)
# params(image, pxNeiborhoodDiameter, std in color space, std in pixel space)

plot.subplot(221)
plot.imshow(img)
plot.title('Original')

plot.subplot(222)
plot.imshow(result)
plot.title('Averaging')

plot.subplot(223)
plot.imshow(medBlur)
plot.title('median blur')

plot.subplot(224)
plot.imshow(bilatBlur)
plot.title('bilateral blur')

plot.show()

