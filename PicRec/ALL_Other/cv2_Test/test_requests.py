# -*- coding: utf-8 -*-
import requests

url = 'https://www.ccofashion.com/products/asymmetric-hem-plain-casual-cardigans?_pos=1&_sid=ebcf9aa34&_ss=r'
url = 'https://www.woshes.com/collections/sweatshirt/products/90a924175d89'
res = requests.get(url)
print(res.status_code)
