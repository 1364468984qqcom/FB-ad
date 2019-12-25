# _*_coding:utf-8_*_
import os
import datetime

# 年-月-日 时：分：秒
now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# 年
year_time =datetime.datetime.now().strftime('%y')
# 年-月
month_time = datetime.datetime.now().strftime('%m')
# 年-月-日
daytime = datetime.datetime.now().strftime('%d')
# 时：分：秒
hourtime = datetime.datetime.now().strftime("%H:%M:%S")
# print(now_time + "\n"+daytime + "\n" + hourtime)


pwd ="\\"+year_time+"\\"+month_time+"\\"+daytime
print(pwd)
# 文件路径
word_name = os.path.exists(pwd)
# 判断文件是否存在：不存在创建
if not word_name:
    os.makedirs(pwd)