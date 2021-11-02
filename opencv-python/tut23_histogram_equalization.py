# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html
# histograms -2: histogram equalization

import numpy as np
import cv2
from matplotlib import pyplot as plot

# equalization can be done in numpy or cv

img = cv2.imread('unequalized-hawkes.jpg')
#img = cv2.imread('happy-face.jpg')
#img = cv2.imread('opencv-logo2.png')
img = cv2.resize(img, None, fx = 1/2, fy = 1/2, interpolation = cv2.INTER_CUBIC)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist, bins = np.histogram(imgGray.flatten(),256,[0,256])

# cumulative distribution function
cdf = hist.cumsum()
cdfNormalized = cdf * hist.max() / cdf.max()

plot.subplot(221),plot.imshow(imgGray, cmap = 'gray')
plot.title('unequalized image')
plot.subplot(222),plot.plot(cdfNormalized, color = 'b')
plot.subplot(222),plot.hist(imgGray.flatten(), 256,[0,256], color = 'r')
plot.xlim([0,256])
plot.title('unequalzied histogram & cdf')
plot.legend(('cdf','histogram'), loc = 'upper left')
#plot.show()


# equalization using masked arrays
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')

img2 = cdf[imgGray]

# now show the equalized image and histogram
hist2, bins2 = np.histogram(img2.flatten(),256,[0,256])


cdf2 = hist2.cumsum()
cdfNormalized2 = cdf2 * hist2.max() / cdf2.max()

plot.subplot(223),plot.imshow(img2, cmap = 'gray')
plot.title('equalized image')
plot.subplot(224),plot.plot(cdfNormalized2, color = 'b')
plot.subplot(224),plot.hist(img2.flatten(), 256,[0,256], color = 'r')
plot.xlim([0,256])
plot.title('equalzied histogram & cdf')
plot.legend(('cdf','histogram'), loc = 'upper left')
plot.show()

# all the above can be done simply in openCV

equalGray = cv2.equalizeHist(imgGray)
res = np.hstack((imgGray,equalGray)) # stack images side by side for comparison
cv2.imshow('openCV equalzied image',res)
cv2.waitKey()

