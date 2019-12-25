# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
img = cv.imread('D:\WorkProject\ImageProject\PicRec\ImagePY\img16.jpg',cv.IMREAD_GRAYSCALE)
img = np.sqrt(img/float(np.max(img)))

