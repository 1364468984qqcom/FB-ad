# -*- coding: utf-8 -*-
"""
一：逻辑运算
opencv自带图片色素的处理函数：
与：bitwise_add()
或：bitwise_or()
非：bitwise_not()
异或：bitwise_xor()
"""
import cv2 as cv
import numpy as np


# 逻辑运算：与或非的操作
def luo_image(scr11, scr22):
    src = cv.bitwise_and(scr11, scr22)  # 与，两张图片同一位置的色素两个值均不为零的才会有输出
    cv.imshow('yu', src)
    src = cv.bitwise_or(scr11, scr22)  # 或 两张图片同一位置的色素两个值不全为零的才会有输出
    cv.imshow('or', src)
    src = cv.bitwise_not(scr22, scr11)  # 非，若同一张照片取反
    cv.imshow('not', src)
    src = cv.bitwise_xor(scr11, scr22)  # 异 两张图片同一位置的色素两个值有一个为零，另一个不为零才会输出
    cv.imshow('nor', src)


scr1 = cv.imread('D:\WorkProject\ImageProject\PicRec\ImageFile\img11.jpg')
scr2 = cv.imread('D:\WorkProject\ImageProject\PicRec\ImageFile\img12.jpg')
cv.imshow('1', scr1)
cv.imshow('2', scr2)
luo_image(scr1, scr2)
cv.waitKey()
cv.destroyAllWindows()
