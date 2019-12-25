# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

"""
模板匹配：通俗讲就是以图找图，通过图中的一部分来找它在图中的位置
"""


# 模板匹配
def template_image():
    tpl = cv.imread('D:\WorkProject\ImageProject\PicRec\ImageFile\img13.png')
    target = cv.imread('D:\WorkProject\ImageProject\PicRec\ImageFile\img12.jpg')

    cv.imshow('模板 a', tpl)
    cv.imshow('原图 b', target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_col, max_col = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_col
        else:
            tl = max_col
        br = (tl[0] + tw, tl[1] + th)
        cv.rectangle(target, tl, br, (0, 0, 225), 2)
        cv.imshow('匹配 c' + np.str(md), target)


template_image()
cv.waitKey()
cv.destroyAllWindows()
