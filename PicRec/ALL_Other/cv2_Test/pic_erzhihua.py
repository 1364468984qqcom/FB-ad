# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

"""
图像二值化：基于图像的直方图来实现的。0为白色1为黑色
"""


def pic_er_zhi_hua(src):
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.imshow('gray:', gray)

    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print('阈值：', ret)
    cv.imshow('OTSU:', binary)

    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    print('阈值：', ret)
    cv.imshow('Triangcle', binary)

    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
    print('阈值：', ret)
    cv.imshow('zi_dingyi_：', binary)

    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_TOZERO_INV)
    print('阈值：', ret)
    cv.imshow('zdy_fanse', binary)

    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_TRUNC)
    print('阈值：', ret)
    cv.imshow('jieduan_1', binary)

    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_TOZERO)
    print('阈值：', ret)
    cv.imshow('jieduan_2:', binary)


if __name__ == '__main__':
    src1 = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img12.jpg')
    cv.namedWindow('yunatu_1', cv.WINDOW_NORMAL)
    cv.imshow('yuantu_2', src1)
    pic_er_zhi_hua(src1)
    cv.waitKey()
    cv.destroyAllWindows()
