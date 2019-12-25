# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

"""
cv2实现pic的合并和切割/填充
"""


def pic_split_merge_fill(src1):
    src2 = src1[10:90, 100:200]
    cv.imshow('jiequ:', src2)
    src1[105:185, 120:220] = src2
    cv.imshow('he_chen:', src1)


if __name__ == '__main__':
    src1 = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img11.jpg')
    cv.imshow('yuanTU_:', src1)
    pic_split_merge_fill(src1)
    cv.waitKey()
    cv.destroyAllWindows()
