# coding=utf-8
# cv2解决绘制中文乱码
import cv2 as cv
import numpy as np


def inverse(image):
    dst = cv.bitwise_not(image)  # 调用bitwise_not函数运行时间非常快！
    cv.imshow('pic4', dst)


src = cv.imread('img7.jpg')
cv.namedWindow('原来', cv.WINDOW_NORMAL)
cv.imshow('原来', src)
t1 = cv.getTickCount()
inverse(src)
t2 = cv.getTickCount()

time = (t2 - t1) * 1000 / cv.getTickFrequency()

print('运行时间：', time)
cv.waitKey()
cv.destroyAllWindows()
