# # -*- coding: utf-8 -*-
#
# import smtplib
# from email.header import Header
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart
# import yagmail
#
#
# def send_email_by_qq(to):
#     """
#     通过QQ方式发送
#     :param to:
#     :return:
#     """
#     sender_mail = '1364468984@qq.com'
#     sender_pass = 'uokfkvqrvyncgdjg'  # QQ邮箱的授权码
#
#     ## 设置总的邮件体对象，对象类型为mixed
#     msg_root = MIMEMultipart('mixed')
#     msg_root['From'] = '1364468984@qq.com'
#     msg_root['To'] = to
#
#     subject = 'PythonQQ邮箱测试'
#     msg_root['subject'] = Header(subject, 'utf-8')
#
#     # 构造文本内容
#     text_info = 'hello,email and smtplib'
#     text_sub = MIMEText(text_info, 'plain', 'utf-8')
#     msg_root.attach(text_sub)
#
from email.mime.text import MIMEText
from email.header import Header
import smtplib

"""
第三方服务
"""
mail_host = "smtp.163.com"  # QQ邮箱的服务器
mail_user = '男同学'
mail_pass = 'uokfkvqrvyncgdjg'

sender = '1364468984@qq.com'
receievers = ['13518160542@163.com']
message = MIMEText('python 邮箱测试是否生效', 'utf-8')
message['From'] = Header('zjc1', 'utf-8')
message['To'] = Header('测试', 'utf-8')

subject = 'python Smtp 邮件测试'

message['Sunject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receievers, message.as_string())
    print('发送成功')
except Exception as w:
    print(w)
