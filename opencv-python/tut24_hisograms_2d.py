# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_histograms/py_2d_histogram/py_2d_histogram.html
# histograms 3: 2d histograms

import cv2
import numpy as np
from matplotlib import pyplot as plot

img = cv2.imread('T-rex.jpg')
#img = cv2.imread('happy-face.jpg')
imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([imghsv],[0,1], None, [180, 256], [0,180, 0,256])

print(hist.size)

# now plot histogram
from matplotlib import pyplot as plot

plot.imshow(hist, interpolation = 'nearest')

#plot.hist(hist)
plot.title('histogram of T-rex image')
plot.xlabel('saturation')
plot.ylabel('hue')
plot.show()
# due to sharp peaks in the histogram things are not scaled well

# try taking log scale to 'flatten out' the histogram display
hist = hist+1 # add 1 to entire array to ensure no zeros exist when taking log
flatHist = np.log(hist)

plot.imshow(flatHist, interpolation = 'nearest')

#plot.hist(hist)
plot.title('log histogram of T-rex image')
plot.xlabel('saturation')
plot.ylabel('hue')
plot.show()
