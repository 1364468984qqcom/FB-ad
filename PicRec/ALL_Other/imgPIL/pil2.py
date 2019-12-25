# -*- coding: utf-8 -*-

from PIL import Image

im = Image.open('D:\WorkProject\ImageProject\PicRec\ImageFile\img16.jpg')
# n_im = Image.new('RGB', (404, 505), 'green')
# n_im.show()
print(im.size)

assert isinstance(im, Image.Image)
# im.show()
box = (400,500,666,666)
region = im.crop(box)
region.show()