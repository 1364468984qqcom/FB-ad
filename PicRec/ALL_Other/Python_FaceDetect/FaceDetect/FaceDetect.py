from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import time


# 由于直接用opencv显示中文会乱码，所以先将图片格式转化为PIL库的格式，用PIL的方法写入中文，然后在转化为CV的格式
def change_cv2_draw(image, strs, local, sizes, colour):
    cv2img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pilimg = Image.fromarray(cv2img)
    draw = ImageDraw.Draw(pilimg)
    font = ImageFont.truetype("SIMYOU.TTF", sizes, encoding="utf-8")  # SIMYOU.TTF为字体文件
    draw.text(local, strs, colour, font=font)
    image = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
    return image


# src为输入的图像
# classifier为对应识别物体的分类器
# strs为识别出的物体的中文说明
# colors表示框的颜色
# minSize为识别物体的最小尺寸，当识别的物体尺寸低于这个尺寸，则不检测，就当没识别到
# minSize为识别物体的最大尺寸，当大于该尺寸时不识别
def myClassifier(src, classifier, strs, colors, minSize, maxSize):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # detectMultiScale()方法里面的参数在另一篇博客中有详解：https://blog.csdn.net/GottaYiWanLiu/article/details/90442274
    obj = classifier.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=minSize, maxSize=maxSize)
    for (x, y, w, h) in obj:
        cv2.rectangle(src, (x, y), (x + w, y + w), colors, 2)  # 画框，（x,y）为识别物体的左上角顶点，（w，h）为宽和高
        src = change_cv2_draw(src, strs, (x, y - 20), 20, colors)  # 显示中文
    return src


# 读取视频文件 若 cap=cv2.VideoCapture(0)，则为获取摄像头画面
cap = cv2.VideoCapture("001.mp4")

# 读取对应物体的训练数据，  注意，以下这些训练数据仅对本视频文件有较好的识别概率，其他场景不行
# 其他场景中，需要重新使用大量到的样本数据去训练，本程序只是一个示例教程

juzuo = cv2.CascadeClassifier("juzuo.xml")  # 局座人脸的训练数据
dajin = cv2.CascadeClassifier("dajin.xml")  # 大紧人类的训练数据
volvo = cv2.CascadeClassifier("volvo.xml")  # 沃尔沃汽车的训练数据
volkswagen = cv2.CascadeClassifier("volkswagen.xml")  # 大众汽车的训练数据

while True:
    _, frame = cap.read()
    frame = myClassifier(frame, juzuo, "局座", (0, 0, 255), (40, 40), (60, 60))
    frame = myClassifier(frame, dajin, "大紧", (0, 255, 0), (40, 40), (70, 70))
    frame = myClassifier(frame, volvo, "沃尔沃", (255, 0, 0), (35, 35), (70, 70))
    frame = myClassifier(frame, volkswagen, "大众", (0, 255, 255), (40, 40), (70, 70))

    cv2.imshow("frame", frame)
    cv2.waitKey(30)
