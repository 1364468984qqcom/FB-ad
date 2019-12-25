import cv2 as cv
import numpy as np


def add_sub_mul_div(src1, src2):
    src = cv.add(src1, src2)  # 相加
    cv.imshow('add', src)
    src = cv.subtract(src1, src2)  # 减
    cv.imshow('sub:', src)
    src = cv.multiply(src1, src2)  # 乘
    cv.imshow('mul:', src)
    src = cv.divide(src1, src2)  # 除
    cv.imshow('div', src)


if __name__ == '__main__':
    src1 = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img11.jpg')
    src2 = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img12.jpg')
    # add_sub_mul_div(src2, src1)
    cv.imshow('yuan_tu_1', src1)
    cv.imshow('yuantu_2', src2)

    add_sub_mul_div(src1, src2)
    cv.waitKey()
    cv.destroyAllWindows()
