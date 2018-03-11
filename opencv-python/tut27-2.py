# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
# template matching - multiple occurances

import cv2
import numpy as np

img_rgb = cv2.imread('mario-coins.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('coin.jpg',0)

height, width = template.shape[:2]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + width, pt[1] + height), (0,0,255), 1)

cv2.imshow('result',img_rgb)
cv2.waitKey()
