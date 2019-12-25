# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np


def laplian_Pic(src):
    dst = cv.Laplacian(src, cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow('dst:', lpls)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img11.png')
cv.namedWindow('yunatu_1', cv.WINDOW_NORMAL)
cv.imshow('yuantu_2', src)
laplian_Pic(src)
cv.waitKey()
cv.destroyAllWindows()
