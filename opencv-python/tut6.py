# python3 script using openCV
# simple image operations

import cv2
import numpy as np

img = cv2.imread('robots.jpg')

px = img[100,100]
print(px)
# prints out [b g r] values

bluePx = img[100,100,0]
print(bluePx)

# better way to access pixels
px = img.item(10,10,2) # red pixel at (10,10)
print(px)

img.itemset((10,10,2),100) # set red px value to 100

# general image properties
print('image shape is: ')
print( img.shape ) # not a method call so no brackets

print('image size is ')
print (img.size )

print('image data type is ')
print( img.dtype )

print('zoom in of robot head')
head = img[50:350, 300:500]

cv2.imshow('robotHead',head)
cv2.waitKey(0)

# splitting bgr channels
b,g,r = cv2.split(img)
# or 
b = img[:,:,0]

# merging back together
imgAgain = cv2.merge((b,g,r)) # need double brackets

# adding border (often used for convolution padding)
cv2.copyMakeBorder(img, 10,10,10,10, cv2.BORDER_CONSTANT) 
#params(image, borderWidths, borderType)
''' BORDER_CONSTANT
	BORDER_REFLECT
	BORDER_REFLECT_101
	BORDER_REPLICATE
	BORDER_WRAP
'''
from matplotlib import pyplot as plot

replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=[255,0,0])

plot.subplot(231),plot.imshow(img,'gray'), plot.title('ORIGINAL')
plot.subplot(232),plot.imshow(replicate,'gray'), plot.title('REPLICATE')
plot.subplot(233),plot.imshow(reflect,'gray'), plot.title('REFLECT')
plot.subplot(234),plot.imshow(reflect101,'gray'), plot.title('REFLECT_101')
plot.subplot(235),plot.imshow(wrap,'gray'), plot.title('WRAP')
plot.subplot(236),plot.imshow(constant,'gray'), plot.title('CONSTANT')

plot.show()