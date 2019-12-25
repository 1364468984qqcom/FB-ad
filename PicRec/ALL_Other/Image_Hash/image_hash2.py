# -*- coding:utf-8 -*-

"""

用dhash判断是否相同照片
基于渐变比较的hash
hash可以省略(本文省略)
By Guanpx

"""

"""
具体注释见上代码
1.通过listdir列出目录内文件，通过后缀集合(postFix)进行图片格式检查
2.每个图片转换为灰度图片并压缩大小 便于处理
3.得到每个像素的value(0-255)
4.每一个像素点与它左边的像素点进行比较，得到0或者1
5.比较结果存入diff后放在allDiff中
6.暴力比较每两张图片的汉明距离
7.设定汉明距离的范围 得出重复图片
"""

from PIL import Image
from os import listdir


def picPostfix():  # 相册后缀的集合
    postFix = set()
    postFix.update(['bmp', 'jpg', 'png', 'tiff', 'gif', 'pcx', 'tga', 'exif',
                    'fpx', 'svg', 'psd', 'cdr', 'pcd', 'dxf', 'ufo', 'eps', 'JPG', 'raw', 'jpeg'])
    return postFix


def getDiff(width, high, image):  # 将要裁剪成w*h的image照片
    diff = []
    im = image.resize((width, high))
    # convert()是图像实例对象的一个方法，接受一个 mode 参数，用以指定一种色彩模式
    imgray = im.convert('L')  # 转换为灰度图片 便于处理
    pixels = list(imgray.getdata())  # 得到像素数据 灰度0-255

    for row in range(high):  # 逐一与它左边的像素点进行比较
        rowStart = row * width  # 起始位置行号
        for index in range(width - 1):
            leftIndex = rowStart + index
            rightIndex = leftIndex + 1  # 左右位置号
            diff.append(pixels[leftIndex] > pixels[rightIndex])

    return diff  # *得到差异值序列 这里可以转换为hash码*


def getHamming(diff=[], diff2=[]):  # 暴力计算两点间汉明距离
    hamming_distance = 0
    for i in range(len(diff)):
        if diff[i] != diff2[i]:
            hamming_distance += 1

    return hamming_distance


if __name__ == '__main__':

    width = 32
    high = 32  # 压缩后的大小
    dirName = "D:\WorkProject\ImageProject\PicRec\ImageFile"  # 相册路径 不是单个图片路径
    allDiff = []
    postFix = picPostfix()  # 图片后缀的集合

    dirList = listdir(dirName)
    cnt = 0
    for i in dirList:
        cnt += 1
        print(cnt)
        # 可以不打印 表示处理的文件计数
        if str(i).split('.')[-1] in postFix:  # 判断后缀是不是照片格式
            im = Image.open(r'%s\%s' % (dirName, str(i)))  # python2:unicode(str(i), "utf-8")----->python3只要str（i）即可
            diff = getDiff(width, high, im)
            allDiff.append((str(i), diff))

    for i in range(len(allDiff)):
        for j in range(i + 1, len(allDiff)):
            if i != j:
                ans = getHamming(allDiff[i][1], allDiff[j][1])
                if ans <= 5:  # 判别的汉明距离，自己根据实际情况设置
                    print(allDiff[i][0], "and", allDiff[j][0], "maybe same photo...")
