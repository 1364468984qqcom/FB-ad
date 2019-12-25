# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np


def nextrace_object_demo():
    video_path = 'D:\File\VideoFile\\numpy.flv'
    capture = cv.VideoCapture(video_path)  # 导入视频
    while 1:
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  ##转换色彩空间为hsv
        # 设置白色的范围,跟踪视频的白色
        lower_hsv = np.array([0, 0, 221])  # 设置过滤的颜色的低值
        upper_hsv = np.array([180, 30, 255])  # 设置过滤颜色的高值

        # 调节图像颜色信息（H）、饱和度（S）、亮度（V）区间，选择白色区域
        msk = cv.inRange(hsv, lower_hsv, upper_hsv)
        cv.imshow('video', frame)
        cv.imshow('mask', msk)
        if cv.waitKey(50) & 0xFF == ord('q'):
            break


nextrace_object_demo()
cv.waitKey()
cv.destroyAllWindows()

