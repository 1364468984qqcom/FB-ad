# -*- coding: utf-8 -*-


import cv2 as cv
import numpy as np

"""
使用拉普拉斯算子测试

前两个是必须的参数：
第一个参数是需要处理的图像；
第二个参数是图像的深度，-1表示采用的是与原图像相同的深度。目标图像的深度必须大于等于原图像的深度；
"""

img = cv.imread('D:\WorkProject\ImageProject\PicRec\OpenCV-python_cv\img_png16.png')
cv.imshow('yuanTu:', img)
# ksize = 3 可以让结果更加清晰
gray_lap = cv.Laplacian(img, cv.CV_16S, ksize=3)
dst = cv.convertScaleAbs(gray_lap)

cv.imshow('LapLacian:', dst)
cv.waitKey()
cv.destroyAllWindows()
