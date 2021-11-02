# python3 script using opencv

import cv2
import numpy as np
from matplotlib import pyplot as plot

img = cv2.imread('robots.jpg')

height, width = img.shape[:2]

# affine transformations
# choose three points in original image, then decide their locations in resultant image
points1 = np.float32([[50,50],[200,200],[50,200]])
points2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(points1,points2)

result = cv2.warpAffine(img,M,(width,height))

plot.subplot(121)
plot.imshow(img)
plot.title('original image')
plot.subplot(122)
plot.imshow(result)
plot.title('afffine transform')
plot.show()

# perspective transform
img = cv2.imread('sudoku.jpg',0)
height, width = img.shape[:2]

# points1 gets mapped to points2
points1 = np.float32([[347,324],[1188,317],[282,1083],[1234,1083]])
points2 = np.float32([[0,0],[1400,0],[0,1400],[1400,1400]])

M = cv2.getPerspectiveTransform(points1,points2)
result = cv2.warpPerspective(img,M,(width,height))

plot.subplot(121)
plot.imshow(img)
plot.title('original image')
plot.subplot(122)
plot.imshow(result)
plot.title('perspective transform')
plot.show()
