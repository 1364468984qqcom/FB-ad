# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

"""
调用bitwise_not函数运行时间非常快！
"""


def insverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow('qufan：', dst)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img16.jpg')
cv.namedWindow('yuan_tu_1:', cv.WINDOW_NORMAL)
cv.imshow('yuna_tu_2', src)
t1 = cv.getTickCount()
insverse(src)
t2 = cv.getTickCount()

time = (t2 - t1) / cv.getTickFrequency()
print('time:%s' % time)
cv.waitKey()
cv.destroyAllWindows()
