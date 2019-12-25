# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import time


# 由于直接用opencv显示中文会乱码，所以先将图片格式转化为PIL库的格式，
# 用PIL的方法写入中文，然后在转化为CV的格式
def change_cv2_draw(image, strs, local, sizes, colour):
    cv2img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pilimg = Image.fromarray(cv2img)
    draw = ImageDraw.Draw(pilimg)
    font = ImageFont.truetype("SIMYOU.TTF", sizes, encoding='utf-8')  # SIMYOU.TTF为字体文件
    draw.text(local, strs, colour, font=font)
    image = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
    return image


"""
1.src为输入的图像
2.classifier为对应识别物体的分类器
3.strs为识别出的物体的中文说明
4.colors为框的颜色
5.minSize为识别物体的的最小尺寸，当识别的物体尺寸低于这个尺寸，则不检测，就没有识别到。
6.maxSize为识别物体的最大尺寸，当大于该尺寸的物体不识别
"""


def myClassifier(src, classifier, strs, colors, minSize, maxSize):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # detectMultiScale()方法里面的参数在另一篇博客中有详解：
    # https://blog.csdn.net/GottaYiWanLiu/article/details/90442274
    """
    其中classifier.detectMultiScale(gray, faceRect, 1.1d, 2, 2, new Size(20, 20), new Size());各个参数说明：
    去官网看了一下说明，结合其他人的博客，
    gray为输入的灰度图
    faceRect为被检测到的物体的矩形向量组，保存有x,y,w,h四个参数，，比如我们检测到人脸，首先我们需要知道这个人脸的位置，
    其次，我们需要知道这个人脸的大小，那么（x,y）就是被检测到的人脸的左上角的坐标，而w,h分别代表宽度和高度
    scaleFactor默认为1.1，scaleFactor的值必须大于1，这个参数的作用，
    好像与识别速度和精度有关，相当于一个阈值，当值越大，识别速度就越快，越容易识别出对象，但精度就会下降，可能会误识别成其他的对象，当值越小，
    识别速度就越慢，相应的精度就会提高，不容易出现将其他物体识别成我们需要的物体，但是容易造成一个都识别不到的情况。
    第一个2为minNeighbors,看别人的博客说是指每个人脸起码被检测到两次才认为被检测到
    第二个2为flags，新版的不需要，老版好像和性能优化有关，不知道理解的对不对
    第一个new Size（20,20）为检测目标的最小尺寸minSzie，低于这个尺寸的对象不检测
    第二个new Size（）为目标的最大尺寸maxSize，高于这个尺寸的对象不检测
    """
    # obj = classifier.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=minSize, maxSize=maxSize)
    obj = classifier.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=minSize, maxSize=maxSize)
    # for (x,y,w,h) in obj:

