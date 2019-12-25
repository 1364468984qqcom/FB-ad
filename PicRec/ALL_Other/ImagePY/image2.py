# -*- coding: utf-8 -*-
import cv2.cv2 as cv

import numpy as np

src = cv.imread('D:/File/ImageProcess/img5.jpg')
# cv2.imshow('dress',src)
# cv2.waitKey(100000)
cv.namedWindow('dress1',2)
cv.imshow('dress',src)
cv.waitKey(0)
cv.destroyAllWindows()

