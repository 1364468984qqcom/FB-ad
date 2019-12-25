# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt

"""
分水岭算法

"""


def water_pic(src):
    print(src.shape)
    blurred = cv.pyrMeanShiftFiltering(src, 10, 100)  # 去除噪点

    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('er_zhi_hua:', binary)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    cv.imshow('xing_tai_cao_zuo:', sure_bg)

    dist = cv.distanceTransform(mb, cv.DIST_L2, 3)
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow('dist_output:', dist_output * 70)

    ret, surface = cv.threshold(dist, dist.max() * .6, 255, cv.THRESH_BINARY)
    cv.imshow('xun_zhao:', surface)

    surface_fg = np.uint8(surface)
    unknown = cv.subtract(sure_bg, surface_fg)
    ret, markers = cv.connectedComponents(surface_fg)
    print(ret)

    markers += 1
    markers[unknown == 255] = 0
    markers = cv.watershed(src, markers=markers)
    src[markers == -1] = [0, 0, 255]
    cv.imshow('fenshuiling', src)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img12.jpg')
cv.namedWindow('yuan_TU_1', cv.WINDOW_NORMAL)
cv.imshow('yuan_tu_2', src)
water_pic(src)
cv.waitKey()
cv.destroyAllWindows()
