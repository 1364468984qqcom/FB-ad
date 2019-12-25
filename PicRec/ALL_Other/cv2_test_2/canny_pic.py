# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np


def edge_Pic(src):
    gray = cv.cvtColor(cv.GaussianBlur(src, (3, 3), 0), cv.COLOR_BGR2GRAY)
    xgard = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    ygard = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    edge_out = cv.Canny(xgard, ygard, 50, 150)
    cv.imshow('canny:', edge_out)
    dst = cv.bitwise_and(src, src, mask=edge_out)
    cv.imshow('color:', dst)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img11.png')
cv.namedWindow('yuanTU1:', cv.WINDOW_NORMAL)
cv.imshow('yuan_tu_2', src)
edge_Pic(src)
cv.waitKey()
cv.destroyAllWindows()
