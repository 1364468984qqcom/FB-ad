# -*- coding: utf-8 -*-
from PIL import Image

imgPath = 'D:\WorkProject\ImageProject\PicRec\ImageFile\img16.jpg'
img = Image.open(imgPath)

assert isinstance(img, Image.Image)
# img.show()
img.save('D:\WorkProject\ImageProject\PicRec\ImageFile\img_png16.png')
im = Image.open('D:\WorkProject\ImageProject\PicRec\ImageFile\img_png16.png')
assert isinstance(im, Image.Image)
print(im.size, im.mode, im.format)
print()
print(img.mode)
new_im = im.convert('P')  # 要将原图片的mode改变之前需要赋值给一个新的变量
print()
print(new_im.mode)
print()
# new_im.show()
assert isinstance(im, Image.Image)
print(new_im.palette)  # <PIL.ImagePalette.ImagePalette object at 0x0000022761C092B0>
print(im.palette)  # None
print()
img1 = Image.open('D:\WorkProject\ImageProject\PicRec\ImageFile\img14.jpg')
assert isinstance(img1, Image.Image)
print(img1.info)  # 打印info之前需要open图片，负责返回为None


