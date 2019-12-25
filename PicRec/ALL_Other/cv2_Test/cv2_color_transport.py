# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np


def numpy_color_transport(src):
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.imshow('huidu_pic:', gray)
    hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
    cv.imshow('hsv_pic:', hsv)
    yuv = cv.cvtColor(src, cv.COLOR_BGR2YUV)
    cv.imshow('yuv_pic:', yuv)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img16.jpg')
cv.namedWindow('yuan_tu:', cv.WINDOW_NORMAL)
cv.imshow('yuantu_2', src)
numpy_color_transport(src)
cv.waitKey()
cv.destroyAllWindows()
