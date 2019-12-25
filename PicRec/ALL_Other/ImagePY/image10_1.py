# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

"""
floodFill填充函数函数

说明如下：
floodFill函数：漫水填充算法：我觉得叫颜色替换好一些
官方定义为：floodFill(InputOutputArray image, Point seedPoint, Scalar newVal, Rect* rect=0, Scalar loDiff=Scalar(), Scalar upDiff=Scalar(), int flags=4 ) 
不知道为啥，python中调用这个函数，Rect* rect=0这个参数没有，剩下7个参数 
通俗解释：floodFill( 1.操作的图像, 2.掩模, 3.起始像素值，4.填充的颜色, 5.填充颜色的低值， 6.填充颜色的高值 ,7.填充的方法)
"""


# 指定颜色替换

def fill_image(image):
    copyImage = image.copy()  # 复制原图像
    h, w = image.shape[:2]  # 读取图像的宽度和高度
    mask = np.zeros([h + 2, w + 2], np.uint8)  # 新建图像矩阵，+2是官方要求
    cv.floodFill(copyImage, mask, (50, 200), (0, 100, 255), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow('tianCong', copyImage)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\ImagePY\img7.jpg')
cv.imshow('src', src)
fill_image(src)
cv.waitKey()
cv.destroyAllWindows()


def fill2_image(image):
    copyImage = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h + 2, w + 2], np.uint8)
