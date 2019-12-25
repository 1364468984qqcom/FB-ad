# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np


# 自定义一张单通道的图片
def create_image():
    img = np.ones([400, 400, 1], np.uint8)
    img = img * 127
    cv.imshow('pic3', img)


create_image()
cv.waitKey()
cv.destroyAllWindows()
