# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

"""
粗略调整图片的对比度和亮度
"""


def add_weight_(src1, a, g):
    height, weight, chennel = src1.shape
    src2 = np.zeros([height, weight, chennel], src1.dtype)
    dst = cv.addWeighted(src1, a, src2, 1 - a, g)
    cv.imshow('demo:', dst)


src1 = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img11.jpg')
cv.namedWindow('yuan_tu-1', cv.WINDOW_NORMAL)
cv.imshow('yuantu_1:', src1)
add_weight_(src1, 10, 50)
cv.waitKey()
cv.destroyAllWindows()
