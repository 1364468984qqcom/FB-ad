# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as mp

"""
计算图片的平均阈值
"""


def average_pic_threshold(src):
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.imshow('gray:', gray)
    h, w = gray.shape[:2]
    m = mp.reshape(gray, [1, w * h])
    mean = m.sum() / (w * h)
    print('mean:', mean)
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.imshow('erzhi:', binary)


if __name__ == '__main__':
    src1 = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img12.jpg')
    cv.namedWindow('yuan_tu_1', cv.WINDOW_NORMAL)
    cv.imshow('yuan_tu_2', src1)
    average_pic_threshold(src1)
    cv.waitKey()
    cv.destroyAllWindows()
