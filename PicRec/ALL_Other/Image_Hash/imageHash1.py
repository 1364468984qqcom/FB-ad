# -*- coding: utf-8 -*-
import imagehash
from PIL import Image
picPath = 'D:\WorkProject\ImageProject\PicRec\ImageFile\img15.jpg'

img = Image.open(picPath)

pHash = imagehash.phash(picPath)
print(pHash)
