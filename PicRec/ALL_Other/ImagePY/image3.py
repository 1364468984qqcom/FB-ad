
# # -*- coding=GBK -*-
# import cv2 as cv
#
# src = cv.imread('img7.jpg')
# # cv.namedWindow('1', 1001)  # ���Բ�ʹ��
# cv.imshow('�·�', src)
# cv.waitKey(0)
# # cv.destroyAllWindows()  # ���Բ���

import cv2 as cv
import numpy as np


# #����һ�����������ͼƬ��һЩ����
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
cv.imwrite('D:\WorkProject\ImageProject\PicRec\ImageFile\\img1.jpg', src)  # ͼƬ���Ϊ����Ҫ�浽c�̣�ҪȨ�޵�
cv.waitKey()
cv.destroyAllWindows()
