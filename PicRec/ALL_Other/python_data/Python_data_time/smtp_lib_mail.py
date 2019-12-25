# -*- coding: utf-8 -*-

import smtplib
from email.header import Header
from email.mime.text import MIMEText

sender_addr = '1364468984@qq.com'
to_addr = ['13518160542@163.com', ]

send_text = MIMEText('我是张金灿，我是一个大傻逼')
send_text['From'] = Header('张金灿1', 'utf-8')  # 发送者
send_text['To'] = Header('张金灿2', 'utf-8')  # 接受者

subject = 'python STMP邮件测试'
send_text['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('125.71.76.218')
    smtpObj.sendmail(sender_addr, to_addr, send_text.as_string())
    print('发送成功')
except:
    print('无法发送邮件')
