# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np


def sobel_pic(src):
    grad_x = cv.Sobel(src, cv.CV_32F, 1, 0)  # x方向
    grad_y = cv.Sobel(src, cv.CV_32F, 0, 1)  # y方向
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow('x:', gradx)  # 颜色变化在水平分层
    cv.imshow('y:', grady)  # 颜色变化在垂直分层
    gradxy = cv.addWeighted(gradx, .5, grady, .5, 0)
    cv.imshow('grad_xy:', gradxy)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img11.png')
cv.namedWindow('yunatu_1', cv.WINDOW_NORMAL)
cv.imshow('yuan_tu_2', src)
sobel_pic(src)
cv.waitKey()
cv.destroyAllWindows()
