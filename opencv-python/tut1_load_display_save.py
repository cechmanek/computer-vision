# Python3 script using openCV
# loading, displaying, saving images

import numpy as np
import cv2
from matplotlib import pyplot as plot

# load as greyscale
image =cv2.imread("robot-hero-1024x640.jpg",0)

# display, then wait for key press
cv2.imshow('myImage', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# create window, then pass image to it
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save image to new file
cv2.imwrite('gray-robots.jpg', image)

# using plot method to display
plot.imshow(image, cmap = 'gray', interpolation='bicubic')
plot.xticks([]), plot.yticks([]) # hides tick lines on plot edges
plot.show()

# imread() uses bgr, but matplotlib uses rgb. this converts
cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
