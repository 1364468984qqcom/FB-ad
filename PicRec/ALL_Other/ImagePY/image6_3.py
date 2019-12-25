# -*- coding: utf-8 -*-

"""
通道分离、合并，修改某一通道
涉及函数：
split() 将彩色图像分割成3个通道
merge()通道合并
"""
import cv2 as cv
import numpy as np

src = cv.imread('img7.jpg')
cv.namedWindow('src1', cv.WINDOW_NORMAL)
cv.imshow('src2',src)

# 通道分析，输出三个单通道图片
b, g, r = cv.split(src)  # 将彩色图像分割3个通道
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

# 通道合并
src = cv.merge([b, g, r])
cv.imshow('src3', src)

# 修改某一个通道的值
src[:, :, 2] = 100
cv.imshow('src4', src)

cv.waitKey()
cv.destroyAllWindows()
