# -*- coding: utf-8 -*-

import requests

# url = "http://47.89.13.253:8003/pic/ban" #
# 此接口为黑名单功能，传入商品ID或者图片，将其加入黑名单，使得传入的商品或者图片不参与图片查重,
# 返回值为图片链接和对应的正向及镜像哈希值,status为1表明加入黑名单成功,status为0表明加入黑名单失败
# 47.75.16.254
# 47.89.13.253  新服务器网站
# http://47.89.13.253:8003/pic/
url = "http://47.89.13.253:8003/pic/"
url = "http://47.89.13.253:8003/pic/query/2"
headers = {
    'Authorization': 'Token 4b1b3246175864eb5c1d0d532163226ab8d587b8',
    # 'Content-Type': 'application/json'
}

data = {'pid': '65733',
        'images': [
            "https://cbu01.alicdn.com/img/ibank/2019/000/452/11659254000_2128266164.60x60.jpg"
        ],
        # 'callback': '1111111'
        }

res = requests.post(url, data=data, headers=headers)
print(res.text)
