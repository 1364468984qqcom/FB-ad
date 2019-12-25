# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

"""
分水岭分割流程：图像->灰度->二值->距离变换->寻找种子->生成Marker->分水岭变换->输出
"""


# 分水岭算法
def water_image(src):
    print(src.shape)
    blurred = cv.pyrMeanShiftFiltering(src, 10, 100)

    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
    cv.imshow('er_zhi_hua:', binary)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)
    surpe_bg = cv.dilate(mb, kernel, iterations=3)
    cv.imshow('xingtaicuozong:', surpe_bg)

    dist = cv.distanceTransform(mb, cv.DIST_L2, 3)
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow('juli_bianhuan:', dist_output * 70)

    ret, surface = cv.threshold(dist, dist.max() * 0.6, 255, cv.THRESH_BINARY)
    cv.imshow('xunzhao_zhongzi:', surface)

    surface_fg = np.uint8(surface)
    unknown = cv.subtract(surpe_bg, surface_fg)
    ret, markers = cv.connectedComponents(surface_fg)
    print(ret)

    markers += 1
    markers[unknown == 255] = 0
    markers = cv.watershed(src, markers=markers)
    src[markers == -1] = [0, 0, 255]
    cv.imshow('fenshuiling:', src)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\ImagePY\img16.jpg')
cv.imshow('yuanTu:', src)
water_image(src)
cv.waitKey()
cv.destroyAllWindows()
