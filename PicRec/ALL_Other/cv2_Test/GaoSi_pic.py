# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np


# 高斯金字塔
def pyRamid_pic(src1):
    level = 3
    temp = src1.copy()  # 拷贝图片
    pyRamid_img = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyRamid_img.append(dst)
        cv.imshow('Gausi:' + str(i), dst)
        temp = dst.copy()
    return pyRamid_img


# 拉普拉斯金字塔
def lplian_src(src):
    pyRamid_pics = pyRamid_pic(src)

    level = len(pyRamid_pics)
    for i in range(level - 1, -1, -1):
        if (i - 1) < 0:
            # 先对图像进行升采样（将图像尺寸行和列方向增大一倍），然后再进行高斯平滑；
            expand = cv.pyrUp(pyRamid_pics)
            lpls = cv.subtract(src, expand)
            cv.imshow('lpls:' + str(i), lpls)
        else:
            expand = cv.pyrUp(pyRamid_pics[i], dstsize=pyRamid_pics[i - 1].shape[:2])

            expand = cv.pyrUp(pyRamid_pics[i], dstsize=pyRamid_pics[i - 1].shape[:2])
            lpls = cv.subtract(pyRamid_pics[i - 1], expand)
            cv.imshow('lpls' + str(i), lpls)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img11.png')
cv.namedWindow('yuan_tu_1', cv.WINDOW_NORMAL)
cv.imshow('yuantu_2', src)
lplian_src(src)
cv.waitKey()
cv.destroyAllWindows()
