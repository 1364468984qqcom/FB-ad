# -*- coding: utf-8 -*-
# 47.89.13.253  新服务器网站
import requests
#'http://47.75.16.254:8003/pic/'
url = 'http://47.75.16.254:8003/pic/'
data = {
    "pid": 65535,
    "images": [
        "http://img3.imgtn.bdimg.com/it/u=1547947154,2056741993&fm=26&gp=0.jpg",
        "http://img4.imgtn.bdimg.com/it/u=2866533716,2951245878&fm=26&gp=0.jpg"
    ]}

headers = {"Authorization": "Token 4b1b3246175864eb5c1d0d532163226ab8d587b8"}

r = requests.post(url, data=data, headers=headers)
print(r.text)
