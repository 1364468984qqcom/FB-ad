#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import cv2 as cv
import numpy as np


def ruihua_blur_pic(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 锐化
    dst = cv.filter2D(image, -1, kernel=kernel)
    cv.imshow("ruihua_pic", dst)

    dst = cv.blur(image, (12, 10))
    cv.imshow('mohu_pic:', dst)


src = cv.imread("D:\WorkProject\ImageProject\PicRec\cv2_Test\img16.jpg")
cv.namedWindow("yuan_tu_1", cv.WINDOW_NORMAL)
cv.imshow("YUAN_tu_2", src)
ruihua_blur_pic(src)
cv.waitKey()
cv.destroyAllWindows()



