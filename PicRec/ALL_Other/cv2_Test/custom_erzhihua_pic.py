# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

"""
adaptiveThreshold: 自定义阈值，当同一幅图像上的不同部分的具有不同亮度时。
这种情况下我们需要采用自适应阈值。此时的阈值是根据图像上的每一个小区域计算与其对应的阈值。
因此在同一幅图像上的不同区域采用的是不同的阈值，
从而使我们能在亮度不同的情况下得到更好的结果。
"""


def custom_pic(src1):
    gray = cv.cvtColor(src1, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)
    binary1 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow('binary1', binary1)
    binary2 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow('binary2', binary2)


if __name__ == '__main__':
    src1 = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img12.jpg')
    cv.namedWindow('yuan_tu_1', cv.WINDOW_NORMAL)
    cv.imshow('src', src1)
    custom_pic(src1)
    cv.waitKey()
    cv.destroyAllWindows()
