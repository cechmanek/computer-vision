# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_sift_intro/py_sift_intro.html
# SIFT corner detection

# some emprical starting points for parameters
# number of octaves = 4
# scale levels = 5
# sigma = 1.6 (guassian stdev)
# k = sqrt(2)

'''
SIFT algorithm is patented
so it's only in the paid openCV package
'''

import cv2
import numpy as np

img = cv2.imread('blocks.jpg')
height, width = img.shape[:2]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# createa a sift object
sift = cv2.SIFT()

keyPoints = sift.detect(gray,None)

# can find descriptors for each keypoint
kp, descript = sift.detectAndCompute(gray, None)


siftImg = cv2.drawKeypoints(gray,keyPoints)

cv2.imshow('SIFT features',siftImg)
cv2.waitKey()
