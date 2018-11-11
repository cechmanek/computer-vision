# python3 script using openCV
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_gradients/py_gradients.html
# image gradients

import cv2
import numpy as np
from matplotlib import pyplot as plot

img = cv2.imread('threshold.jpg',0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F,0,1,ksize=5)
# 		params(image,depth,xgrad,ygrad,kernelSize)

plot.subplot(2,2,1), plot.imshow(img,cmap = 'gray')
plot.subplot(2,2,2), plot.imshow(laplacian, cmap = 'gray')
plot.subplot(2,2,3), plot.imshow(sobelx, cmap = 'gray')
plot.subplot(2,2,4), plot.imshow(sobely, cmap = 'gray')

plot.show()

'''the output data type, cv2.CV_8U = np.uint8, but Laplacian and Sobel return positive & negative
gradients, so conversion back to grayscale will lose negative slopes to zero.
keep things
'''
img = cv2.imread('opencv-logo2.png',0)
# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

plot.subplot(1,3,1),plot.imshow(img,cmap = 'gray')
plot.title('Original')
plot.subplot(1,3,2),plot.imshow(sobelx8u,cmap = 'gray')
plot.title('Sobel CV_8U')
plot.subplot(1,3,3),plot.imshow(sobel_8u,cmap = 'gray')
plot.title('Sobel abs(CV_64F)')

plot.show()