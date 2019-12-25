# -*- coding: utf-8 -*-

import cv2 as cv

import numpy as np

"""
计算pic 的均值/中值/高斯/双边滤波算法
"""


def mo_img(src1):
    src2 = cv.blur(src1, (5, 5))
    cv.imshow('blur:', src2)

    src3 = cv.medianBlur(src1, 5)
    cv.imshow('medianBlur:', src3)

    src4 = cv.GaussianBlur(src1, (5, 5), 2)
    cv.imshow('GaussianBlur:', src4)
    src5 = cv.bilateralFilter(src1, 5, 5, 2)
    cv.imshow('bil_filter:', src5)


if __name__ == '__main__':
    src1 = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img11.jpg')
    cv.namedWindow('yuan_tu_:', cv.WINDOW_NORMAL)
    cv.imshow('yuan_tu_1', src1)
    mo_img(src1)
    cv.waitKey()
    cv.destroyAllWindows()
