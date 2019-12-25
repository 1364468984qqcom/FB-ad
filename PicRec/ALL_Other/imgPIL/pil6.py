# -*- coding: utf-8 -*-

from PIL import Image

img = Image.open('D:\WorkProject\ImageProject\PicRec\ImageFile\img16.jpg')
assert isinstance(img, Image.Image)
bbox = img.getbbox()
print(bbox)
get_color = img.getcolors()
print(get_color)
get_data = img.getdata()
print(get_data)
get_extrema = img.getextrema()

print(get_extrema)
print()
get_pixel = img.getpixel((0, 0))
print(get_pixel)
hist = img.histogram()
print(hist)