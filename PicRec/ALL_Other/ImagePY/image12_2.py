# -*- coding: utf-8 -*-

import cv2 as cv
from matplotlib import pyplot as plt

"""
  直方图均衡化：提升对比度的两种方法：默认、自定义
"""


# 提升对比度（默认提升），只能是灰度图像
def equalHist_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('原图 a', gray)
    dst = cv.equalizeHist(gray)
    cv.imshow('默认处理 b', dst)


# 对比度限制（自定义提示参数）
def clahe_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # clipLimit是对比度的大小，tileGridSize是每次处理块的大小
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(4, 4))

    dst = clahe.apply(gray)
    cv.imshow('自定义处理 c', dst)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\ImagePY\img7.jpg')
equalHist_image(src)
clahe_image(src)
cv.waitKey()
cv.destroyAllWindows()
