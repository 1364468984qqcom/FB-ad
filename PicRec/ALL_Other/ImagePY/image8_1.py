# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

"""
粗略的调整图片对比度和亮度


基本原理：两张图片合成。
先按照原来的图片的格式新建一个色素全为零的图片，然后按照两张图的比例不同合成一张新图片。
主要用到函数：addWeighted函数

addWeighted函数：官方：计算两个图像阵列的加权和 我的理解是按照所占比例合成两张图片。
addWeighted(InputArray src1, double alpha, InputArray src2, double beta, double gamma, OutputArray dst, int dtype=-1);
一共有七个参数：前4个是两张要合成的图片及它们所占比例，第5个double gamma起微调作用，第6个OutputArray dst是合成后的图片，第七个输出的图片的类型（可选参数，默认-1）
有公式得出两个图片加成输出的图片为：dst=src1*alpha+src2*beta+gamma
"""


def contrast_brightness_image(src1, a, g):
    h, w, ch = src1.shape  # 获取shape的height，weight，channel（通道）

    # 新建全零图片的数组src2，将height和weight，类型设置为原图片的通道类型（色素全为零，即输出黑色）
    src2 = np.zeros([h, w, ch], src1.dtype)
    dst = cv.addWeighted(src1, a, src2, 1 - a, g)  # addWeighted函数说明如上
    cv.imshow('demo', dst)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\ImageFile\img11.jpg')
cv.namedWindow('old', cv.WINDOW_NORMAL)
cv.imshow('old2', src)
contrast_brightness_image(src, 1.2, 10)  # 第一个1.2为对比度  第二个为亮度数值越大越亮
cv.waitKey()
cv.destroyAllWindows()



