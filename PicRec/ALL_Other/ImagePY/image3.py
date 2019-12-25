
# # -*- coding=GBK -*-
# import cv2 as cv
#
# src = cv.imread('img7.jpg')
# # cv.namedWindow('1', 1001)  # 可以不使用
# cv.imshow('衣服', src)
# cv.waitKey(0)
# # cv.destroyAllWindows()  # 可以不用

import cv2 as cv
import numpy as np


# #定义一个函数来输出图片的一些属性
def get_image_info(image):
    print(type(image))
    print()
    print(image.shape)
    print()
    print(image.size)
    print()
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


src = cv.imread('img7.jpg')
cv.imshow('dress', src)
get_image_info(src)
cv.imwrite('D:\WorkProject\ImageProject\PicRec\ImageFile\\img1.jpg', src)  # 图片另存为，不要存到c盘，要权限的
cv.waitKey()
cv.destroyAllWindows()
