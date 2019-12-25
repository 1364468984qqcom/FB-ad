# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np




"""
直线检测

cv2.HoughLinesP()函数原型：
"""
img = cv.imread('D:\WorkProject\ImageProject\PicRec\ImagePY\img30.jpg')
# 灰度处理
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# canny边缘处理
edges = cv.Canny(gray, 50, 120)
line = 100
minLineLength = 20
# HoughLinesP 函数是概率直线检测，注意区分HoughLines函数
lines = cv.HoughLinesP(edges, 1, np.pi / 180, 100, lines=line, minLineLength=minLineLength)
# 降维处理
lines1 = lines[:, 0, :]
# line 函数勾画直线
# (x1,y1),(x2,y2)坐标位置
# （0,255,0）： 设置BGR通道颜色
# 2 是设置颜色粗浅度

for x1, y1, x2, y2 in lines1:
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
# 显示图像
cv.imshow('edges:', edges)
cv.imshow('lines:', img)
cv.waitKey()
cv.destroyAllWindows()




