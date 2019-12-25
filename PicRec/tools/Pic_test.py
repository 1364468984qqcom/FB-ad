# -*- coding: utf-8 -*-

from PIL import Image
import requests
import imagehash
from io import BytesIO


def phash_hanMing(img1, img2):
    res1 = requests.get(img1).content
    res2 = requests.get(img2).content

    image1 = Image.open(BytesIO(res1))
    image2 = Image.open(BytesIO(res2))
    img_hash1 = str(imagehash.dhash(image1.transpose(Image.FLIP_LEFT_RIGHT)))
    img_hash2 = str(imagehash.dhash(image2.transpose(Image.FLIP_LEFT_RIGHT)))
    # rvs_image = image1.transpose(Image.FLIP_LEFT_RIGHT)
    # rvs_image_hash = str(imagehash.phash(rvs_image))
    print('image_hash1:', img_hash1)
    print('image_hash2:', img_hash2)
    print()
    diff = (int(img_hash1, 16)) ^ (int(img_hash2, 16))
    print('汉明距离：', bin(diff).count('1'))


if __name__ == '__main__':
    url1 = 'https://cbu01.alicdn.com/img/ibank/2019/424/434/10936434424_2144762306.jpg'
    url2 = 'https://cbu01.alicdn.com/img/ibank/2019/880/842/10995248088_2144762306.jpg'
    # url1 = 'https://cbu01.alicdn.com/img/ibank/2018/679/441/10051144976_2087646882.60x60.jpg'
    url1 = 'https://product-repository.oss-cn-hongkong.aliyuncs.com/19/10/17/a64b4f5b415edbb37b873bc44327dd14.jpg?x-oss-process=image/resize,m_lfit,h_320,w_320'
    url2 = 'https://product-repository.oss-cn-hongkong.aliyuncs.com/19/10/17/a64b4f5b415edbb37b873bc44327dd14.jpg?x-oss-process=image/resize,m_lfit,h_320,w_320'

    url1 = 'http://product-repository.oss-cn-hongkong.aliyuncs.com/19/10/30/e15825a5885338857d55890b389019f6.jpg'
    url2 = 'http://product-repository.oss-cn-hongkong.aliyuncs.com/19/10/30/60d880af944605cbad9c9303a9f303a6.jpg'
    # url1='C:\\Users\\ADMIN\\Desktop\\2.jpg'
    # url2='C:\\Users\\ADMIN\\Desktop\\1.jpg'

    phash_hanMing(url1, url2)

a = ["b11e61b623366dc3", "dd44b3dc3c9291f0", "bc9ec3b293328963", "b09ae69a66cb638c", "b13661b661366dc6",
     "b13661b661366dc6", "e99ec2a697328963", "bc9ec3b2b3324943", "e99ec2a697328963"]

b = ["9fe57c636130219b", "99cca5dc6b944a35", "8db038cc4cdecccd", "b489cb8bd9646633", "b193cbcd8c661267",
     "a5cbcd8e9a303969", "b6c69b9999658c64", "b0ccc74ec793cc98", "b0ccc74ecf938c98", "e56d866ece869838",
     "e56d866ece869838", "a96db55494e25a36", "e1ce9421cc99b3e6", "9f8771b87e17a110", "9de770937198ce88"]
