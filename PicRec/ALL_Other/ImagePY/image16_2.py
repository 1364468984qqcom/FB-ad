# -*- coding: utf-8 -*-

import cv2 as cv

"""
1.scharr算子和拉普拉斯算子
2019.9.23
"""

# # scharr算子
# def scharr_image(image):
#     grad_x = cv.Scharr(image,cv.CV_32F,1,0) # x方向导数
#     grad_y = cv.Scharr(image,cv.CV_32F,0,1) # y方向的导数
#     gradx = cv.convertScaleAbs(grad_x)
#     grady = cv.convertScaleAbs(grad_y)
#     cv.imshow('x方向：',gradx) # 颜色变化在水平分层
#     cv.imshow('y方向：',grady) # 颜色变化在垂直方向分层
#     gradxy = cv.addWeighted(gradx,0.5,grady,0.5,0)
#     cv.imshow('hecheng:',gradxy)
# img = cv.imread('D:\WorkProject\ImageProject\PicRec\ImagePY\img16.jpg')
# cv.imshow('yuantu：',img)
# scharr_image(img)
# cv.waitKey()
# cv.destroyAllWindows()
#


"""
拉普拉斯算子
2019.9.23
"""


def lapalian_image(image):
    dst = cv.Laplacian(image, cv.CV_32F)
    lapls = cv.convertScaleAbs(dst)
    cv.imshow('lpls：', lapls)


img = cv.imread('D:\WorkProject\ImageProject\PicRec\ImagePY\img16.jpg')
cv.imshow('yuantu：', img)
lapalian_image(img)

cv.waitKey()
cv.destroyAllWindows()
