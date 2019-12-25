# -*- coding: utf-8 -*-
import cv2
import cv2 as cv
import numpy as np
img = cv.imread('D:\WorkProject\ImageProject\PicRec\ImageFile\img15.jpg')


aver = np.mean(img)
print('aver',aver)

img_sh = img[104,699]
print(img_sh)