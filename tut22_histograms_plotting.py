#http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_histograms/py_histogram_begins/py_histogram_begins.html
# histograms -1: find plot analyize

import numpy as np
import cv2

# cv2.calcHist([images], [channels], mask, [histSize], ranges[hist[accumulate]])
# channels is which color channel to find the hist of,
# for a grayscale image pass[0], for color image pass 0,1, or 2 for b,g, or r
# for full image hist mask = NONE, else choose a section
# hist size is number of bins, ie [256] for full range, [8] for bins 0-31,32-63, etc
# range is range of histogram, [0-256]



img = cv2.imread('helicopter.jpg')
#img = cv2.imread('happy-face.jpg')
#img = cv2.imread('opencv-logo2.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

grayHist = cv2.calcHist(imgGray,[0],None,[256],[0,256])

blueHist = cv2.calcHist(img,[0],None,[256],[0,256])
greenHist = cv2.calcHist(img,[1],None,[256],[0,256])
redHist = cv2.calcHist(img,[2],None,[256],[0,256])

# plotting histograms, which are 256 x 1 arrays
from matplotlib import pyplot as plot

cv2.imshow('original image',img)
'''
plot.subplot(221),plot.plot(grayHist)
plot.title('gray histogram')
plot.subplot(222),plot.hist(imgGray.ravel(),256,[0,256])
plot.show()
cv2.waitKey()
'''
colors =('b','g','r')
for i,col in enumerate(colors):
	hist = cv2.calcHist([img],[i],None,[256],[0,256])
	plot.plot(hist, color = col)
	plot.xlim([0,256]) # set plot bound

plot.title('bgr histogram of original image')
plot.show()
cv2.waitKey()

# can also use numpy for histograms, but cv is much faster
hist, bins = np.histogram(img.ravel(),256,[2,256])
# bins contains all the available values, so here is 257 elements long, 0-256

# a faster computation is:
hist = np.bincount(img.ravel(),minlength=256)

# masking images to only look at sections for histogram

myMask = np.zeros(img.shape[:2], np.uint8) # create full black image
#myMask[100:300,100:400] = 255 # set this fixed region of interest in the middle white
# can also set region of interest based on image size, uncomment above line to have complex shapes
myMask[round(img.shape[0]/4):round(img.shape[0]*3/4), round(img.shape[1]/4):round(img.shape[1]*3/4)] = 255

maskedImg = cv2.bitwise_and(imgGray,imgGray,mask = myMask)


fullHist = cv2.calcHist([imgGray], [0],None,[256],[0,256])
maskHist = cv2.calcHist([imgGray],[0], myMask, [256],[0,256])

plot.subplot(221), plot.imshow(imgGray, 'gray')
plot.subplot(222), plot.imshow(myMask, 'gray')
plot.subplot(223), plot.imshow(maskedImg, 'gray')
plot.subplot(224), plot.plot(fullHist, color = 'b'), plot.plot(maskHist, color = 'g')
plot.xlim([0,256])

plot.show()
