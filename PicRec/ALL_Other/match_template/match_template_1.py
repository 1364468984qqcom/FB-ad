# -*- coding: utf-8 -*-
import cv2
import numpy as np
# np.where>2
img1 = cv2.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img11.jpg')
template = cv2.imread('D:\WorkProject\ImageProject\PicRec\cv2_Test\img12.jpg')
h, w = template.shape[:2]  # row=h,col=w
res = cv2.matchTemplate(img1,template,cv2.TM_CCOEFF)
min_val ,max_val,min_loc,max_loc = cv2.minMaxLoc(res)

left_top = max_loc
right_bottom = (left_top[0]+w,left_top[1]+h)
cv2.rectangle(img1,left_top,right_bottom,255,2)