# -*- coding: utf-8 -*-

import cv2 as cv

"""
色彩空间的转换
HSV色彩空间说明：
H：0-180  S: 0-255 V： 0-255
"""


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # RGB转换为gray
    cv.imshow('gray:', gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)  # RGB转换为hsv
    cv.imshow('hsv:', hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)  # RGB转换为yuv
    cv.imshow('yuv', yuv)


src = cv.imread('img7.jpg')
cv.namedWindow('原来', cv.WINDOW_NORMAL)
cv.imshow('原来:', src)
color_space_demo(src)
cv.waitKey()
cv.destroyAllWindows()
