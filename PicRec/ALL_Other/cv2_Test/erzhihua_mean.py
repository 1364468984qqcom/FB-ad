# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

"""
计算图像的均值作为阈值来二值化
故阈值又叫临界值
图像的二值化，就是将图像上的像素点的灰度值设置为0或255，
也就是将整个图像呈现出明显的只有黑和白的视觉效果
"""


def custom_erZhiHua_mean(src1):
    gray = cv.cvtColor(src1, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)
    h, w = gray.shape[:2]  # 只要获取图片的宽高属性。不需要他的通道
    m = np.reshape(gray, [1, w * h])  # 转为为一维数组
    mean = m.sum() / (w*h)
    print('mean', mean)
    ret, binary = cv.threshold(src1, mean, 255, cv.THRESH_BINARY)
    cv.imshow('binary ', binary)


src1 = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img16.jpg')
cv.namedWindow('yuantu_1', cv.WINDOW_NORMAL)
cv.imshow('yuan_tu_2', src1)
custom_erZhiHua_mean(src1)
cv.waitKey()
cv.destroyAllWindows()
