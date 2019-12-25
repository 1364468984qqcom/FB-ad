# -*- coding: utf-8 -*-


# 图片色素的数值运算(加减乘除)和逻辑运算(与或非异或)
"""
数值运算
一：数值运算
opencv自带图片色素的处理函数：
相加：add()    
相减：subtract()    
相乘：multiply() 
相除：divide()   
原理就是：通过获取两张（一次只能是两张）个图片的同一个位置的色素值来实现运算。
运算的要求：两张图片的shape要一样。
例图：（若想用下面两张图可另存为图片，若保存的文件无后缀，添加后缀为.jpg即可）
"""
import cv2 as cv


# 数值运算；加减乘除
def shu_image(src11, src22):
    src = cv.add(src11, src22)  # 加
    cv.imshow('+：', src)

    src = cv.subtract(src11, src22)  # 减
    cv.imshow('-:', src)

    src = cv.multiply(src11, src22)  # 乘
    cv.imshow('*：', src)

    src = cv.divide(src11, src22)  # 除
    cv.imshow('/:', src)


src1 = cv.imread('D:\WorkProject\ImageProject\PicRec\ImageFile\img11.jpg')
src2 = cv.imread('D:\WorkProject\ImageProject\PicRec\ImageFile\img12.jpg')

cv.imshow('img11', src1)
cv.imshow('img12', src2)

shu_image(src1, src2)
cv.waitKey()
cv.destroyAllWindows()
