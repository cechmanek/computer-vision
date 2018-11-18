# python3 script using openCV
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html
# geometric transforms of images

import cv2
import numpy as np
from matplotlib import pyplot as plot

img = cv2.imread('robots.jpg')

res1 = cv2.resize(img, None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)

# OR

height, width = img.shape[:2]

res2 = cv2.resize(img, (3*width,2*height), interpolation = cv2.INTER_CUBIC)


plot.subplot(1,2,1)
plot.imshow(res1)
plot.title('method 1')
plot.subplot(1,2,2)
plot.imshow(res2)
plot.title('method 2')

plot.show()
print('Note: images are scaled in the display window. Look at axes to determine size')

# translating images
'''
apply a matrix transformation M:
M = [1 0 tx
	 0 1 ty]
'''
M = np.float32([[1,0,100], [0,1,50]])
dst = cv2.warpAffine(img,M,(width,height))
#		params(image, transform, newImgSize)
			
cv2.imshow('translated imge', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# rotating images
M = cv2.getRotationMatrix2D((width/2,height/2),90,1)

dst = cv2.warpAffine(img,M,(width,height))
cv2.imshow('rotated imge', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

