# -*- coding: utf-8 -*-
from PIL import Image

img = Image.open('D:\WorkProject\ImageProject\PicRec\ImageFile\img16.jpg')
assert isinstance(img, Image.Image)
box = [0, 0, 111, 111]
im_region = img.crop(box)

print(im_region.size, im_region.mode, im_region.info)

assert isinstance(img, Image.Image)
img.paste(im_region, (111, 111))
img.paste(im_region, (400, 400, 511, 511))
img.show()
