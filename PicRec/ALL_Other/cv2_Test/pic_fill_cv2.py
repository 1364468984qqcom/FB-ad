# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

"""
指定颜色作为填充
"""


def fill_to_pic_part(src1):
    copy_src1 = src1.copy()  # 复制原图片
    h, w = src1.shape[:2]
    mask = np.zeros([h + 2, w + 2], np.uint8, src1.dtype)
    cv.floodFill(copy_src1, mask, (0, 80), (0, 100, 255), (100, 100, 255), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow('tian_chong', copy_src1)


if __name__ == '__main__':
    src1 = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img11.jpg')
    cv.imshow('yuan_tu_1', cv.WINDOW_NORMAL)
    cv.imshow('yuantu_1', src1)
    fill_to_pic_part(src1)
    cv.waitKey()
    cv.destroyAllWindows()
