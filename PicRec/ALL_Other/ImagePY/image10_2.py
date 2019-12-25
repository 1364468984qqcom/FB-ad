# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

"""
#指定位置填充
"""


def fill2_image():
    image = np.zeros([200, 200, 3], np.uint8)
    cv.imshow('old', image)
    mask = np.ones([202, 202, 1], np.uint8)
    mask[100:150, 100:150] = 0
    cv.floodFill(image, mask, (100, 100), (0, 0, 225), cv.FLOODFILL_MASK_ONLY)

    cv.imshow('tiancong2', image)


# src = cv.imread('D:\WorkProject\ImageProject\PicRec\ImageFile\img12.jpg')
# cv.imshow('yuantu', src)
fill2_image()
cv.waitKey()
cv.destroyAllWindows()
