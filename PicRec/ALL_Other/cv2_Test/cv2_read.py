# -*- coding: utf-8 -*-

import cv2 as cv

src = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img16.jpg')
cv.namedWindow('src', 0)
cv.imshow('src2', src)
cv.waitKey()
cv.destroyAllWindows()
