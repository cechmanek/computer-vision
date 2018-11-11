# python3 script using opencv
#image thresholding - Otsu's binarization
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html

import cv2
import numpy as np
from matplotlib import pyplot as plot

# load image as grayscale
img = cv2.imread('lena_denoise_noisy.jpg',0)

# global threshold for comparision
ret, threshImg1 = cv2.threshold(img,127,255, cv2.THRESH_BINARY)

# otsu's threshold based on asumed bimodal histogram
ret2, threshImg2 = cv2.threshold(img,0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# otsu's after gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
#	params(image, filterSize, filterMean)
ret3, threshImg3 = cv2.threshold(blur, 0,255, cv2.THRESH_BINARY+ cv2.THRESH_OTSU)

# plot everything
titles = ['original', 'histogram','global threshold', 
		  'original', 'histogram','Otsu\'s',
		  'blurred', 'histogram', 'Otsu\'s after gauss filter']
images = [img,0, threshImg1,
		  img, 0, threshImg2,
		  blur,0, threshImg3]

for i in range(3):
	plot.subplot(3,3,i*3+1)
	plot.imshow(images[i*3],'gray')
	plot.title(titles[i*3])
	plot.xticks([]), plot.yticks([])
    
	plot.subplot(3,3,i*3+2)
	plot.hist(images[i*3].ravel(),256)
	plot.title(titles[i*3+1])
	plot.xticks([]), plot.yticks([])
    
	plot.subplot(3,3,i*3+3)
	plot.imshow(images[i*3+2],'gray')
	plot.title(titles[i*3+2])
	plot.xticks([]), plot.yticks([])
	
plot.show()