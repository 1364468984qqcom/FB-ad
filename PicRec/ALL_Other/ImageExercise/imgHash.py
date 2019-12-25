# -*- coding: utf-8 -*-

import imagehash
from PIL import Image
import requests

from io import BytesIO

imgUrl = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1568009981620&di=6291537882191ae42515c50736a8559c&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201504%2F26%2F201504263326_tYanN.jpeg'

res = requests.get(imgUrl).content  # 只要二进制数据

img = Image.open(BytesIO(res))
print(img)
img_hash = str(imagehash.whash(img))
print(img_hash)
