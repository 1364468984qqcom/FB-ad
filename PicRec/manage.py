#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dja.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# 请求地址：/pic/
# 请求方式：POST
# 请求头：Authorization Token 4b1b3246175864eb5c1d0d532163226ab8d587b8
#         Content-Type application/json
# 携带参数：
#     pid     -> 产品编号
#     images            -> 产品图集
#     callback   -> 回调地址