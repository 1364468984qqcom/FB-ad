# -*- coding: utf-8 -*-
import cv2 as cv

import numpy as np

"""
自定义模糊
"""


def filter_2d_custom(src1):
    kernel1 = np.ones((8, 7), np.float) / 25  # 自定义矩阵，并且防止数据溢出
    src2 = cv.filter2D(src1, -1, kernel1)
    cv.imshow('kernel:', src2)

    kernel2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0],[0,-1,5],[5,1,0]], np.float32)
    src2 = cv.filter2D(src1, -1, kernel2)
    cv.imshow('kernel2:', src2)


if __name__ == '__main__':
    src1 = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img11.jpg')
    cv.imshow('yuantu_', src1)
    cv.namedWindow('yuna_tu_', cv.WINDOW_NORMAL)
    filter_2d_custom(src1)
    cv.waitKey()
    cv.destroyAllWindows()
