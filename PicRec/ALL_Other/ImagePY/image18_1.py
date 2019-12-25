# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np


# 霍夫直线检测
def line_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 将bgr图像转换为灰度图像
    edges = cv.Canny(gray, 50, 150, apertureSize=3)  # canny处理的图像必须是灰度图像
    lines = cv.HoughLines(edges, 1, np.pi / 180, 200)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow('zhiXian:', image)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\ImagePY\img30.jpg')
cv.imshow('yuanTu：', src)
line_image(src)
cv.waitKey()
cv.destroyAllWindows()
