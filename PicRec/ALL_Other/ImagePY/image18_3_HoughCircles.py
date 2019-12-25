# -*- coding: utf-8 -*-
"""
圆脸检测
圆检测
HoughCircles函数原型
"""

import cv2 as cv
import numpy as np

planets = cv.imread('D:\\WorkProject\\ImageProject\\PicRec\\ImagePY\\img21.jpg')
# 灰度处理
gray_img = cv.cvtColor(planets, cv.COLOR_BGR2GRAY)
# 平滑模糊处理
img = cv.medianBlur(gray_img, 5)

# 灰度图像转成彩色图像
cimg = cv.cvtColor(img, cv.COLOR_GRAY2RGB)

# 圆检测
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=50, maxRadius=100)
# 转化为整数
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # 勾画图形，planets图形，i[0],i[1],圆心坐标，i[2]是半径
    cv.circle(planets, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # 勾画圆心，圆心实质也是一个半径为2的圆形
    cv.circle(planets, (i[0], i[1]), 2, (0, 0, 255), 3)

cv.imwrite('plantes_cirsles.jpg', planets)
cv.imshow('mypic:', cimg)
cv.imshow('HoughCircle:', planets)
cv.waitKey()
cv.destroyAllWindows()
