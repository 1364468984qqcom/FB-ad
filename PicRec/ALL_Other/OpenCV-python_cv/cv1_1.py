# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

"""
轮廓检测:
"""
img = cv.imread('D:\WorkProject\ImageProject\PicRec\OpenCV-python_cv\img_png16.png')
cv.imshow('yuanTu:',img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, (0, 0, 255), 3)
cv.imshow('img:', img)
cv.waitKey()
cv.destroyAllWindows()
