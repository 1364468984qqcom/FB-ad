# -*- coding: utf-8 -*-

import cv2
import requests
import numpy as np

# imgPath = r"D:\WorkProject\ImageProject\PicRec\ImagePY\img7.jpg"

img = cv2.imread('./img7.jpg')
cv2.imshow('phone', img)

img1 = cv2.imwrite('./img1113333331.png',img)
cv2.waitKey(5000)  # 等待多少豪秒关闭
