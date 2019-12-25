# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

"""
图片切割、合并、填充  指定位置填充，大小要一样才能填充  请仔细看下面的数字大小规律

原理通过操作图像矩阵来获取或合并指定位置的图像
"""


# 截取图片中的指定区域或在指定区域添加某一图片
def jie_image(src1):
    src2 = src1[5:89, 200:280]  # 截取第5行到89行的第500列到630列的区域
    cv.imshow("截取", src2)
    src1[105:189, 100:180] = src2  # 指定位置填充，大小要一样才能填充
    cv.imshow("合成", src1)


src = cv.imread("D:\WorkProject\ImageProject\PicRec\ImagePY\img7.jpg")
h, w, ch = src.shape
print(h, w, ch)
cv.imshow("原来", src)
jie_image(src)
cv.waitKey(0)
cv.destroyAllWindows()
