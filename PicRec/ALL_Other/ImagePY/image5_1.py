# -*- coding: utf-8 -*-

"""
读取一张图片，修改颜色通道后输出

可以得到图像的：行数,列数,通道数的矩阵,对矩阵进行操作可改变图像像素
"""
import cv2 as cv
import numpy as np


def access_pixles(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channel = image.shape[2]
    print('height:{},width:{},channel:{}'.format(height, width, channel))
    for row in range(height):
        for col in range(width):
            for c in range(channel):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pic", image)


src = cv.imread('img7.jpg')
cv.imshow('dress', src)
t1 = cv.getTickCount()  # 毫秒级别的计时函数,记录了系统启动以来的时间毫秒
access_pixles(src)
t2 = cv.getTickCount()
time = (t2 - t1) * 1000 / cv.getTickFrequency()  # getTickFrequency用于返回CPU的频率,就是每秒的计时周期数
print('运行时间为：', time)
cv.waitKey()
cv.destroyAllWindows()
