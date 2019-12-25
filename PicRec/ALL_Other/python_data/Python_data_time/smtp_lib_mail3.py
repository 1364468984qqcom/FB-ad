# -*- coding: utf-8 -*-

import yagmail


def mail():
    userName = '13518160542@163.com'
    passWd = 'zjc123456'
    contents = '测试发送附件'
    try:
        yag = yagmail.SMTP(userName, passWd, host='smtp.163.com')  # smtp_ssl=True
        yag.send(['728163448@qq.com', '1364468984@qq.com'], '测试发送附件', contents,
                 ['D:\WorkProject\ImageProject\PicRec\ImagePY\kebo.jpeg',
                  'D:\WorkProject\ImageProject\PicRec\ImagePY\img16.jpg'])
    except Exception as e:
        print('无法发送')
        print(e)
    print('ok')


if __name__ == '__main__':
    mail()
"""
"""

# import yagmail
#
# # 链接邮箱服务器
# yag = yagmail.SMTP(user='13518160542@163.com', password="zjc123456", host='smtp.163.com')
#
# # 邮箱正文
# contents = ['This is the body, and here is just text http://somedomain/image.png',
#             'You can find an audio file attached.', '/local/path/song.mp3']
#
# # 发送邮件
# yag.send('1364468984@qq.com', 'subject', contents)
# import itertools
# # for i in itertools.count(0):
# #     print(i)
