# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

"""
自定义模糊
"""


def zi_image(src1):
    kernel1 = np.ones((5, 5), np.float) / 25  # 自定义矩阵，防止数值溢出
    src2 = cv.filter2D(src1, -1, kernel1)
    cv.imshow('自定义均值模糊 a', src2)

    kernel2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    src2 = cv.filter2D(src1, -1, kernel2)
    cv.imshow('自定义锐化 b', src2)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\ImagePY\img7.jpg')
cv.imshow('原图 c', src)
zi_image(src)
cv.waitKey()
cv.destroyAllWindows()
