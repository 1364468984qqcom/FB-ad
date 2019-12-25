# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np


def color_split(src):
    b, g, r = cv.split(src)
    cv.imshow('b:', b)
    cv.imshow('g', g)
    cv.imshow('r', r)

    src = cv.merge([b, g, r])
    cv.imshow('hebing：', src)

    src[:, :, 2] = 100
    cv.imshow('dan_tong_dao', src)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img16.jpg')
cv.namedWindow('yuantu_1', cv.WINDOW_NORMAL)
cv.imshow('yuantu_2', src)
color_split(src)
cv.waitKey()
cv.destroyAllWindows()
