# -*- coding: utf-8 -*-

from PIL import Image

# ImageChops模块包含一些算术图形操作，叫做channel operations（“chops”）。
# 这些操作可用于诸多目的，比如图像特效，图像组合，算法绘图等等。
# 通道操作只用于8位图像（比如“L”模式和“RGB”模式）。
from PIL import ImageChops

# from PIL import  ImageCrackCode #ImageCrackCode模块允许用户检测和测量图像的各种特性。
# 这个模块只存在于PIL Plus包中。我目前安装的PIL中没有包含这个模块。

# ImageDraw模块为image对象提供了基本的图形处理功能。
# 例如，它可以创建新图像，注释或润饰已存在图像，为web应用实时产生各种图形。
from PIL import ImageDraw

# ImageEnhance模块包括一些用于图像增强的类。它们分别为Color类、Brightness类、Contrast类和Sharpness类。
from PIL import ImageEnhance

# ImageFile模块为图像打开和保存功能提供了相关支持功能。
# 另外，它提供了一个Parser类，这个类可以一块一块地对一张图像进行解码（例如，网络联接中接收一张图像）。
# 这个类的接口与标准的sgmllib和xmllib模块的接口一样。
from PIL import ImageFile

# ImageFileIO模块用于从一个socket或者其他流设备中读取一张图像。
# 不赞成使用这个模块。在新的code中将使用ImageFile模块的Parser类来代替它。
# from PIL import ImageFileIO

# ImageFilter模块包括各种滤波器的预定义集合，与Image类的filter方法一起使用。
# 该模块包含这些图像增强的滤波器:
# BLUR，CONTOUR，DETAIL，EDGE_ENHANCE，EDGE_ENHANCE_MORE，EMBOSS，FIND_EDGES，SMOOTH，SMOOTH_MORE和SHARPEN。
from PIL import ImageFilter

# ImageFont模块定义了一个同名的类，即ImageFont类。
# 这个类的实例中存储着bitmap字体，需要与ImageDraw类的text方法一起使用。
# PIL使用自己的字体文件格式存储bitmap字体。
# 用户可以使用pilfont工具包将BDF和PCF字体描述器（Xwindow字体格式）转换为这种格式。
# PIL Plus包中才会支持矢量字体。

from PIL import ImageFont

# (New in1.1.3)ImageGrab模块用于将屏幕上的内容拷贝到一个PIL图像内存中。
# 当前的版本只在windows操作系统上可以工作

from PIL import ImageGrab

# (New in1.1.3)ImageOps模块包括一些“ready-made”图像处理操作。
# 它可以完成直方图均衡、裁剪、量化、镜像等操作。
# 这个模块somewhat experimental，大多数操作只工作在L和RGB图像上。
from PIL import ImageOps

# ImagePath模块用于存储和操作二维向量数据。Path对象将被传递到ImageDraw模块的方法中。
from PIL import ImagePath

# ImageSequence模块包括一个wrapper类，它为图像序列中每一帧提供了迭代器
from PIL import ImageSequence

