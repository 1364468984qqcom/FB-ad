# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

"""
高斯金字塔和拉普拉斯金字塔

要求：拉普拉斯金字塔时，图像大小必须是2的n次方*2的n次方，不然会报错
"""


#  pyrDown()先对图像进行高斯平滑，然后再进行降采样（将图像尺寸行和列方向缩减一半）；
# pyrUp()函数  先对图像进行升采样（将图像尺寸行和列方向增大一倍），然后再进行高斯平滑；

# 高斯金字塔
def pyramid_image(image):
    level = 3  # 金字塔的层数
    temp = image.copy()  # 拷贝图像
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow('高斯金字塔 a' + str(i), dst)
        temp = dst.copy()
    return pyramid_images


# 拉普拉斯金字塔
def laplian_image(image):
    pyramid_images = pyramid_image(image)
    level = len(pyramid_images)
    for i in range(level - 1, -1, -1):
        if (i - 1) < 0:
            expand = cv.pyrUp(pyramid_images[i], dstsize=image.shape[:2])
            lpls = cv.subtract(image, expand)
            cv.imshow('拉普拉斯 b' + str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i - 1].shape[:2])
            lpls = cv.subtract(pyramid_images[i - 1], expand)
            cv.imshow('拉普拉斯 c' + str(i), lpls)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\ImagePY\img15.jpg')
cv.imshow('原图 d', src)
laplian_image(src)
cv.waitKey()
cv.destroyAllWindows()
