# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

"""
图像二值化：基于图像的直方图来实现的，0白色 1黑色
"""


def threshold_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('原图 a', gray)

    # 大律法,全局自适应阈值 参数0可改为任意数字但不起作用
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print('阈值 b', ret)
    cv.imshow('OTSU b', binary)

    # TRIANGLE法,，全局自适应阈值, 参数0可改为任意数字但不起作用，适用于单个波峰
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    print('阈值 c', ret)
    cv.imshow('TRIANGLE c', binary)

    # 自定义阈值为150,大于150的是白色 小于的是黑色
    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
    print('阈值 d', ret)
    cv.imshow('自定义 d', binary)

    # 自定义阈值为150,大于150的是黑色 小于的是白色
    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
    print('阈值 e', ret)
    cv.imshow('自定义反色 e', binary)

    # 截断 大于150的是改为150  小于150的保留
    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_TRUNC)
    print('阈值 g', ret)
    cv.imshow('截断 g', binary)

    # 截断 小于150的是改为150  大于150的保留
    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_TOZERO)
    print('阈值 i', ret)
    cv.imshow('截断2 i', binary)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\ImagePY\img15.jpg')
threshold_image(src)
cv.waitKey()
cv.destroyAllWindows()
