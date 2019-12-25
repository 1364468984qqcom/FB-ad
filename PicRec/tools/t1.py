import hashlib
from PIL import ImageEnhance, Image
import oss2
import requests
from io import BytesIO
from datetime import datetime

# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。

OSS_ABROAD = 'oss-cn-hongkong.aliyuncs.com'
ACCESS_ID = 'LTAI5OENtxGMLTMw'
ACCESS_KEY = 'bbTvTlqBkWebZtwfmEq2fkgTv5fs4D'
BUCKET = 'product-repository'
ENDPOINT = 'oss-cn-hongkong.aliyuncs.com'

auth = oss2.Auth(ACCESS_ID, ACCESS_KEY)
# Endpoint以杭州为例，其它Region请按实际情况填写。
# daytime = datetime.now().strftime(r'%y/%m/%d')
# dir = 'repush'
# bucket_path = BUCKET + '/' + dir + '/' + daytime

bucket = oss2.Bucket(auth, ENDPOINT, BUCKET)
images_url = [
    'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1572843836951&di=a7cdf36a065717844823d84dbee1539f&imgtype=0&src=http%3A%2F%2Fimg.sccnn.com%2Fbimg%2F337%2F8479.jpg',
]
imgs_url = list()
for url in images_url:
    r = requests.get(url=url)
    image = Image.open(BytesIO(r.content))
    # 图片处理

    enh_sha = ImageEnhance.Sharpness(image)
    sharpness = 3.0  # 锐化度
    image_sharped = enh_sha.enhance(sharpness)
    image_bytes = image_sharped.tobytes()

    # 上传文件

    filename = hashlib.md5(str(datetime.now()).encode('utf-8')).hexdigest() + '.jpg'
    '''
     :param key: 上传到OSS的文件名
    
     :param data: 待上传的内容。
    '''
    print('filename:', filename)

    result = bucket.put_object(filename, image_bytes)

    # result = bucket.put_object_from_file('t2.jgp',
    #                                      r'C:\Users\zy\Desktop\work\t2.jpg')  # 括号内 左边是上传后的文件名，右边是当前系统的文件地址

    print('http status: {0}'.format(result.status))  # 打印上传的返回值 200成功
    jpg_url = bucket.sign_url('GET', filename, 60)  # 阿里返回一个关于Zabbix_Graph.jpg的url地址 60是链接60秒有效

    print(jpg_url)
    imgs_url.append(jpg_url)
print(imgs_url)
