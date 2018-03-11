# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html#fourier-transform
# fourier transform

import cv2
import numpy as np
from matplotlib import pyplot as plot

img = cv2.imread('happy-face.jpg',0)

height, width = img.shape
img = cv2.resize(img,(int(width/3), int(height/3)), interpolation = cv2.INTER_LINEAR) 

# fft of 2d arrays in numpy
myFFT = np.fft.fft2(img) # returns a complex 2d array

centerFFT = np.fft.fftshift(myFFT)
# to change output image size pass new dimensions as tuple
# original image is padded with zeros, or cropped to be smaller
# np.fft.fft2(imgGray, (imgGray.shape[0]+20, imgGray.shape[1]+20))

# by default the zero frequency is at top left corner
#cv2.imshow('orignal image', img)
#cv2.imshow('Fourier Transform, 0 at top left', abs(myFFT)) # need to change dtype to uint8
#cv2.imshow('centered Fourier Transform',20*np.log(abs(centerFFT))) # needs to be uint8
#cv2.waitKey()

plot.imshow(20*np.log(abs(centerFFT)), cmap = 'gray')
plot.title('centered FFT, using plot')
plot.show()

# to use imshow() the data type must be uint8, having values between 0,255 isn't good enough
myArray = np.random.randint(25,size = img.shape, dtype ='uint8')
plot.subplot(121),plot.imshow(myArray, cmap = 'gray')
plot.subplot(122),plot.imshow(img, cmap = 'gray')
plot.show()

# high pass filtering in the frequency domain

img = cv2.imread('Messi.png',0)

rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)

myFFT = np.fft.fft2(img) # returns a complex 2d array
centerFFT = np.fft.fftshift(myFFT) # change the plot origin from top left to center

# set low frequency components in middle of FFT plot to zero
centerFFT[crow-30:crow+30, ccol-30:ccol+30] = 0

f_ishift = np.fft.ifftshift(centerFFT) # shift the centered FFT back to top left
img_back = np.fft.ifft2(f_ishift) # inverse fourier transform
img_back = np.abs(img_back) # resultant highpass filtered image

plot.subplot(131),plot.imshow(img, cmap = 'gray')
plot.title('Input Image'), plot.xticks([]), plot.yticks([])
plot.subplot(132),plot.imshow(img_back, cmap = 'gray')
plot.title('Image after HPF'), plot.xticks([]), plot.yticks([])
plot.subplot(133),plot.imshow(img_back)
plot.title('Result in JET'), plot.xticks([]), plot.yticks([])

plot.show()

######
# the same can be done in openCV
img = cv2.imread('Messi.png',0)

dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitudeSpectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1]))

plot.subplot(121), plot.imshow(img, cmap = 'gray')
plot.title('original image'), plot.xticks([]),plot.yticks([])
plot.subplot(122), plot.imshow(magnitudeSpectrum, cmap = 'gray')
plot.title('Magnitude Spectrum'), plot.xticks([]),plot.yticks([])
plot.show()

#Notes: opencv is generally faster than numpy
# also, image arrays that are sizes of power of 2, 3 or 5 are faster, so pad zeros if speed's an issue

