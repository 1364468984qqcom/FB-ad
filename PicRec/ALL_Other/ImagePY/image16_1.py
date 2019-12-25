# -*- coding: utf-8 -*-
import cv2 as cv


# 图像梯度：索贝尔算子
def sobel_image(image):
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)  # x方向的导数
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)  # y方向的导数
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow('x方向：', gradx)  # 颜色变化在水平分层
    cv.imshow('y方向', grady)  # 颜色变化在垂直分成
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow('hecheng:', gradxy)


img = cv.imread('img16.jpg')
cv.imshow('yuanLai', img)
sobel_image(img)
cv.waitKey()
cv.destroyAllWindows()
