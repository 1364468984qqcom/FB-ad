# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

"""
#画出图像的直方图
"""


def hist_image(image):
    color = ('blue', 'black', 'red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()


src = cv.imread('D:\WorkProject\ImageProject\PicRec\ImagePY\img7.jpg')
cv.namedWindow('原图 a', cv.WINDOW_NORMAL)
cv.imshow('原图 b', src)
hist_image(src)
cv.waitKey()
cv.destroyAllWindows()

