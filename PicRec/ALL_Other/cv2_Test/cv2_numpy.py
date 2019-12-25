# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np


def numpy_cv2(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channel = image.shape[2]

    print('图片的属性：', height, width, channel)
    for row in range(height):
        for col in range(width):
            for c in range(channel):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow('xiu_gai_hou:', image)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img16.jpg')
cv.imshow('yuan_tu:', src)
t1 = cv.getTickCount()  # 毫秒级别的计时函数,记录了系统启动以来的时间毫秒
numpy_cv2(src)
t2 = cv.getTickCount()
time = (t2 - t1) * 1000 / cv.getTickFrequency()  # getTickFrequency用于返回CPU的频率,就是每秒的计时周期数
print('time:%s' % time)
cv.waitKey()
cv.destroyAllWindows()


def numpy_create_pic():
    img = np.ones([400, 400, 3], np.uint8)
    img[:, :, 0] = img[:, :, 0] * 255
    img[:, :, 1] = img[:, :, 1] * 255
    img[:, :, 2] = img[:, :, 2] * 255
    cv.imshow('numpy_create:', img)


numpy_create_pic()
cv.waitKey()
cv.destroyAllWindows()


def numpy_a_create():
    img = np.ones([400, 400, 1], np.uint8)
    img = img * 127
    cv.imshow('zhizhi_pic:', img)


numpy_a_create()
cv.waitKey()
cv.destroyAllWindows()
