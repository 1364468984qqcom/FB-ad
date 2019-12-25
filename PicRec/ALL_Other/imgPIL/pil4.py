# -*- coding: utf-8 -*-
from PIL import Image

img = Image.open('D:\WorkProject\ImageProject\PicRec\ImageFile\img16.jpg')
assert isinstance(img, Image.Image)
bans = img.getbands()

print(bans)  # 打印PIL的图片的通道
print(len(bans))  # 打印PIL的图片的通道数
print(img.mode)
new_img = img.convert('P')
print(new_img.mode)
print(new_img.info)
print(new_img.size)
print(new_img.height)
print(img.size)
new_img2 = img.resize((185, 658), Image.ANTIALIAS)
print(new_img2.size)
# new_img3 = new_img.thumbnail((200, 200))  #有异常
print(img.palette)
print(new_img.width)

img2 = Image.open('D:\WorkProject\ImageProject\PicRec\ImageFile\img14.jpg')
print(img2.size)
assert isinstance(img2,Image.Image)
new_img2 = img2.resize((700,790))
print(new_img2.size)
im = Image.blend(img, img2, 0.5)
assert isinstance(im, Image.Image)
im.show()
