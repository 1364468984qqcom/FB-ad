# -*- coding: utf-8 -*-
import requests
from PIL import Image
import imagehash
from io import BytesIO

"""
phash :感知哈希
"""
url1 = 'https://cbu01.alicdn.com/img/ibank/2018/532/744/9385447235_1712056649.60x60.jpg'
url1 = 'https://cbu01.alicdn.com/img/ibank/2019/654/995/12037599456_350285216.60x60.jpg'
url1 = 'https://cbu01.alicdn.com/img/ibank/2019/249/683/11976386942_350285216.60x60.jpg'
url1 = 'https://cbu01.alicdn.com/img/ibank/2019/847/583/11974385748_350285216.60x60.jpg'
url1 = 'https://cbu01.alicdn.com/img/ibank/2019/294/138/11581831492_692167774.60x60.jpg'
url1 = 'https://cbu01.alicdn.com/img/ibank/2019/750/781/10593187057_2140839991.60x60.jpg'
url1 = 'https://cbu01.alicdn.com/img/ibank/2019/769/252/10619252967_2140839991.60x60.jpg_.webp'
url1 = 'https://cbu01.alicdn.com/img/ibank/2019/671/126/10966621176_2144762306.60x60.jpg'
url1 = 'https://cbu01.alicdn.com/img/ibank/2019/880/842/10995248088_2144762306.60x60.jpg'

url1 = 'https://cbu01.alicdn.com/img/ibank/2019/880/842/10995248088_2144762306.60x60.jpg'

# url2 = 'https://cbu01.alicdn.com/img/ibank/2017/130/410/4830014031_1784114954.60x60.jpg'
# url3 = 'https://cbu01.alicdn.com/img/ibank/2017/129/483/4831384921_1784114954.60x60.jpg'
#
# """
# phash :感知哈希
# """
# resp = requests.get(url1).content
# image = Image.open(BytesIO(resp))
# # phash :感知哈希
# image_hash1 = str(imagehash.phash(image))
# print(image_hash1)
#
# resp = requests.get(url2).content
# image = Image.open(BytesIO(resp))
# # phash :感知哈希
# image_hash2 = str(imagehash.phash(image))
# print(image_hash2)
# print()
# """
# 采用差异哈希比较
# """
# print()
# resp = requests.get(url1).content
# image = Image.open(BytesIO(resp))
# # phash :感知哈希d
# image_hash1 = str(imagehash.dhash(image))
# print(image_hash1)
# print()
# resp = requests.get(url2).content
# image = Image.open(BytesIO(resp))
# # phash :感知哈希
# image_hash2 = str(imagehash.dhash(image))
# print(image_hash2)
resp = requests.get(url1).content
image = Image.open(BytesIO(resp))
# phash :感知哈希
image_hash1 = str(imagehash.phash(image))
print('image_hash1', image_hash1)

# url2 = "https://cbu01.alicdn.com/img/ibank/2017/130/410/4830014031_1784114954.60x60.jpg"
url2 = 'https://cbu01.alicdn.com/img/ibank/2018/911/341/9405143119_1712056649.60x60.jpg'
url2 = 'https://cbu01.alicdn.com/img/ibank/2019/410/040/11934040014_350285216.60x60.jpg'
url2 = 'https://cbu01.alicdn.com/img/ibank/2019/616/636/11904636616_350285216.60x60.jpg'
url2 = 'https://cbu01.alicdn.com/img/ibank/2019/357/193/11974391753_350285216.60x60.jpg'
url2 = 'https://cbu01.alicdn.com/img/ibank/2019/015/528/11581825510_692167774.60x60.jpg'
url2 = 'https://cbu01.alicdn.com/img/ibank/2019/527/151/10593151725_2140839991.60x60.jpg'
url2 = 'https://cbu01.alicdn.com/img/ibank/2019/424/434/10936434424_2144762306.60x60.jpg'

url2 = 'https://cbu01.alicdn.com/img/ibank/2019/424/434/10936434424_2144762306.60x60.jpg'
res = requests.get(url2).content

img = Image.open(BytesIO(res))
img_hash2 = str(imagehash.phash(img))
print('img_hash2:', img_hash2)

difference = (int(image_hash1, 16)) ^ (int(img_hash2, 16))
print('汉明距离：', bin(difference).count('1'))
