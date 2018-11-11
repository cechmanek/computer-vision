# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contours_hierarchy/py_contours_hierarchy.html
# contours hierarchy

import cv2
import numpy as np

img = cv2.imread('nestedContours.png')
img = cv2.imread('opencv-logo2.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bsImg, contours, hierarchy = cv2.findContours(imgGray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

''' hierarchy tells the 'nestedness' of contours:
“Next denotes next contour at the same hierarchical level.”
“Previous denotes previous contour at the same hierarchical level.”
“First_Child denotes its first child contour.”
“Parent denotes index of its parent contour.”

cv2.RETR_LIST returns all contours at the same hierarchy, ie doesn't create relations
cv2.RETR_EXTERNAL returns only the outermost contours
cv2.RETR_CCOMP returns all contours as external or nested. a contour within 2 other contours is a new parent
cv2.RETR_TREE returns full tree of contour relations

hierarchy structure is:
[Next, Previous, First_Child, Parent]

“Next denotes next contour at the same hierarchical level.”
“Previous denotes previous contour at the same hierarchical level.”
“First_Child denotes its first child contour.”
“Parent denotes index of its parent contour.”

if there is no child the field is labelled -1




'''
print('the contour hierarchy is:')
print(hierarchy)

cv2.imshow('gray image',imgGray)
cv2.imshow('original image',img)
cv2.imshow('contour image',bsImg)
cv2.waitKey()
cv2.destroyAllWindows()

