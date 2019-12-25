# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np


def lines_src(src):
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLines(edges, 1, np.pi / 180, 200)
    for line in lines:
        rho, thete = line[0]
        a = np.cos(thete)
        b = np.sin(thete)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow('lines:', src)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img11.png')
cv.namedWindow('yuan_tu_1', cv.WINDOW_NORMAL)
cv.imshow('yuan_tu_2', src)
lines_src(src)
cv.waitKey()
cv.destroyAllWindows()


