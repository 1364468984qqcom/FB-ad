# -*- coding: utf-8 -*-

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

"""
绘制pic直方图
"""


def hist_img(src):
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv.calcHist([src], [i], None, [256], [0, 256])
        plt.plot(hist, color)
        plt.xlim([0, 256])
    plt.show()


if __name__ == '__main__':
    src1 = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img16.jpg')
    cv.namedWindow('yuanTU_', cv.WINDOW_NORMAL)
    cv.imshow('yuantu_', src1)
    hist_img(src1)
    cv.waitKey()
    cv.destroyAllWindows()
