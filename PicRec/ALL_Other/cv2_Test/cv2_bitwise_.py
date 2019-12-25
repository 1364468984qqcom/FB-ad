# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np


def cv2_bitwise(src11, src2):
    res = cv.add(src1, src2)
    cv.imshow('and_res:', res)
    res = cv.bitwise_and(src2, src1)
    cv.imshow('and：', res)
    res = cv.bitwise_or(src1, src2)
    cv.imshow('or:', res)
    res = cv.bitwise_not(src1, src2)  # 对一张图片取反操作
    cv.imshow('not', res)
    res = cv.bitwise_xor(src1, src2)
    cv.imshow('xor:', res)


if __name__ == '__main__':
    src1 = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img11.jpg')
    src2 = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img12.jpg')
    # add_sub_mul_div(src2, src1)
    cv.imshow('yuan_tu_1', src1)
    cv.imshow('yuantu_2', src2)
    cv2_bitwise(src1, src2)
    cv.waitKey()
    cv.destroyAllWindows()
