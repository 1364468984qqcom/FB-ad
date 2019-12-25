# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np


def create_image():
    # zeros:double类零矩阵  创建400*400 3个通道的矩阵图像 参数时classname为uint8
    img = np.zeros([400, 400, 3], np.uint8)
    # ones([400, 400])是创建一个400*400的全1矩阵，*255即是全255矩阵
    # 并将这个矩阵的值赋给img的第一维
    img[:, :, 0] = np.ones([400, 400]) * 25805  # 后面的数字可以修改，修改即变颜色
    img[:, :, 1] = np.ones([400, 400]) * 255  # 第二维全是255
    img[:, :, 2] = np.ones([400, 400]) * 20  # 第三维全是255

    cv.imshow('pic2', img)  # 输出一张400*400的白色图片(255 255 255):蓝(B)、绿(G)、红(R)
    cv.imwrite('./img22222.jpg', img)


create_image()
cv.waitKey()
cv.destroyAllWindows()
