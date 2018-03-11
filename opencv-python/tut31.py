# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_grabcut/py_grabcut.html
# interactive foreground extraction

import cv2
import numpy as np
from matplotlib import pyplot as plot

img = cv2.imread('Messi.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
myMask = np.zeros(img.shape[:2], np.uint8)

# create a rectangle containing all the foreground
rect = (45,40,500,825) # top left corner coordinates x,y, width,height 

# empty array that grabCut needs
bgModel = np.zeros((1,65),np.float64)
fgModel = np.zeros((1,65),np.float64)
iterations = 5

cv2.grabCut(img, myMask, rect, bgModel, fgModel, iterations, cv2.GC_INIT_WITH_RECT)
# or
# mask, bgModel, fgModel = cv2.grabCut(img,mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)

myMask2 = np.where((myMask == 2)| (myMask == 0), 0 ,1).astype('uint8')

img = img*myMask2[:,:,np.newaxis]

plot.imshow(img)
plot.colorbar()
plot.show()