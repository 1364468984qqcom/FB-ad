# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np


def scharr_pic(src):
    grad_x = cv.Scharr(src, cv.CV_32F, 1, 0)  # x方向导数
    grad_Y = cv.Scharr(src, cv.CV_32F, 0, 1)  # Y方向的导数
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_Y)
    gradxy = cv.addWeighted(gradx, .5, grady, .5, 0)
    cv.imshow('x:', gradx)
    cv.imshow('y', grady)
    cv.imshow('xy:', gradxy)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img11.png')
cv.namedWindow('yuantu_1', cv.WINDOW_NORMAL)
cv.imshow('yuantu_2', src)
scharr_pic(src)
cv.waitKey()
cv.destroyAllWindows()
