# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

"""
利用卷积对图像模糊处理

看了许多资料，在图像上个人觉得卷积就是：对于某一位置的像素，
通过算法来把它附近的所有像素点的值联合起来，重新设置这个像素的大小。（大概就是这样）
这个算法类似有：均值，中值，就是取周围所有像素的均值、中值来设置这个像素的大小。
（关于边界问题：有几种填充方法：补零、边界复制、块复制、镜像复制等方法） 
"""


def mo_image(src1):
    src2 = cv.blur(src1, (5, 5))
    cv.imshow('均值模糊 a', src2)

    src2 = cv.medianBlur(src1, 5)
    cv.imshow('中值模糊 b', src2)

    src2 = cv.GaussianBlur(src1, (5, 5), 2)
    cv.imshow('高斯模糊c', src2)

    src2 = cv.bilateralFilter(src1, 5, 5, 2)
    cv.imshow('双边滤波d', src2)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\ImagePY\img7.jpg')
cv.namedWindow('原来e', cv.WINDOW_NORMAL)
cv.imshow('原来f', src)
mo_image(src)
cv.waitKey()
cv.destroyAllWindows()
