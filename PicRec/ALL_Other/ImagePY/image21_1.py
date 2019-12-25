# -*- coding: utf-8 -*-
import cv2 as cv


def open_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('er_zhi_hua:', binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow('kai:', binary)


def close_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    cv.imshow('bi:', binary)


src = cv.imread('D:\WorkProject\ImageProject\PicRec\ImagePY\img21.jpg')
cv.imshow('yuanTu:', src)
open_image(src)
close_image(src)
cv.waitKey()
cv.destroyAllWindows()
