# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_histograms/py_histogram_backprojection/py_histogram_backprojection.html
# histograms 4: histogram back projection

import cv2
import numpy as np
from matplotlib import pyplot as plot

''' process for back projection

img = cv2.imread('Messi.png')
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
imgWiththingToFInd = img.copy()


# define a region of interest in the original image
thingToFInd = imghsv[300:400,350:450,:]

imgWiththingToFInd = cv2.rectangle(imgWiththingToFInd, (350,400),(450,300), (0,255,0), 2)
#params(image, firstcorner, second corner, color, linetype)

cv2.imshow('messi',img)
#cv2.imshow('thingToFInd',thingToFInd)
cv2.imshow('messi with thingToFInd',imgWiththingToFInd)
cv2.waitKey()

# find 2d histograms of original image and thingToFInd (thingToFInd aka searchedImage to find)
M = cv2.calcHist([imghsv], [0,1], None, [180,256], [0,180, 0, 256])
I = cv2.calcHist([thingToFInd], [0,1], None, [180,256], [0,180, 0, 256])

h, s, v = cv2.split(thingToFInd)
R = M/I
B = R[h.ravel(),s.ravel()]
B = np.minimum(B,1)
B = B.reshape(thingToFInd.shape[:2])

#now convolve with a circular disc 'D'
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(B,-1,disc,B)
B = np.uint8(B)
cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)

location of maximum is the location of the found object
we can threshold around this region

ret,thresh = cv2.threshold(B,50,255,0)
'''

# back projection in opencv

searchedImage = cv2.imread('Messi.png') # searchedImage area to search
hsvt = cv2.cvtColor(searchedImage,cv2.COLOR_BGR2HSV)

thingToFInd = searchedImage.copy() # thing we are searhing for, in this case it's a subsection of the image
thingToFInd = thingToFInd[300:400,350:450,:]
hsv = cv2.cvtColor(thingToFInd,cv2.COLOR_BGR2HSV)

# resize searchedImage to match image
#searchedImage = cv2.resize(searchedImage, hsv.shape[:2], interpolation = cv2.INTER_CUBIC)

cv2.imshow('thingToFInd',searchedImage)
cv2.imshow('image hsv',hsv)
cv2.waitKey()

# calculating object histogram
thingToFIndhist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )

# normalize histogram and apply backprojection
cv2.normalize(thingToFIndhist,thingToFIndhist,0,255,cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt],[0,1],thingToFIndhist,[0,180,0,256],1)

# Now convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(dst,-1,disc,dst)

# threshold and binary AND
ret,thresh = cv2.threshold(dst,50,255,0)
thresh = cv2.merge((thresh,thresh,thresh))
res = cv2.bitwise_and(searchedImage,thresh)

imgWiththingToFInd = cv2.rectangle(searchedImage, (350,400),(450,300), (0,255,0), 2)

res = np.hstack((imgWiththingToFInd,thresh,res))

smallRes = cv2.resize(res, (int(res.shape[0]),int(res.shape[1]/3)),interpolation = cv2.INTER_LINEAR)

#cv2.imshow('result',res)
cv2.imshow('result: original image, mask, masked image', smallRes)
cv2.waitKey()