# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def classify_gray_hist(src1, src2, size=(256, 256)):
    img1 = cv.resize(src1, size)
    img2 = cv.resize(src2, size)

    hist1 = cv.calcHist([img1], [0], None, [256], [0.0, 256.0])
    hist2 = cv.calcHist([img2], [0], None, [256], [0.0, 256.0])

    plt.plot(range(256), hist1, 'r')
    plt.plot(range(256), hist2, 'b')
    plt.show()

    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - abs(hist1[i] - hist2[i]) / max(hist2[i], hist1[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree


src1 = 'http://product-repository.oss-cn-hongkong.aliyuncs.com/19/10/30/e15825a5885338857d55890b389019f6.jpg'
src2 = 'http://product-repository.oss-cn-hongkong.aliyuncs.com/19/10/30/60d880af944605cbad9c9303a9f303a6.jpg'
print(classify_gray_hist(src1, src2))

# def calcultate(src1,src2):
#     hist1 = cv.calcHist([src1],[0],None,[256],[0.0,256.0])
#     hist2 = cv.calcHist([src2],[0],None,[256],[0.0,256.0])
#
#     degree = 0
