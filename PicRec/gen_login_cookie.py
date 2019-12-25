import json
import time
import redis
import requests
import schedule
import random
import logging
from urllib import parse
from selenium.webdriver.chrome import options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from logging.handlers import RotatingFileHandler
from scrapy.selector import Selector

'''
本地使用，生成cookies
1.登陆频繁微博会出现414,无法访问
2.切换海外代理登陆，新浪微博需要打码，淘宝需要验证手机号

'''


# todo 修改日志

# cookie_error_logger = logging.getLogger('cookie_error_log')
# cookie_info_logger = logging.getLogger('cookie_info_log')
# cookie_error_logger.setLevel(logging.WARNING)
# cookie_info_logger.setLevel(logging.DEBUG)
# ch_error = RotatingFileHandler('get_cookie_error.log', maxBytes=3 * 1024 * 1024, backupCount=1)
# ch_info = RotatingFileHandler('get_cookie_info.log', maxBytes=10 * 1024 * 1024, backupCount=1)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# ch_error.setFormatter(formatter)
# ch_info.setFormatter(formatter)
# cookie_error_logger.addHandler(ch_error)
# cookie_info_logger.addHandler(ch_info)


def get_cookie(account):
    """
    使用微博关联登陆淘宝,进而从m端淘宝页面获取cookie
    """
    username = account.get('username')
    password = account.get('password')
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True, db=0)
    # 本地redis
    reds = redis.Redis(connection_pool=pool)
    option = options.Options()
    option.add_argument("disable-infobars")  # # 去除info框
    option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 开发者模式,防止被识别
    option.add_argument('log-level=3')
    # option.add_argument("--proxy-server=http://114.239.254.76:4236")  #添加代理
    # option.add_argument('--headless')         # headless模式
    # option.add_argument("window-size=2436, 1125")
    # option.add_argument("--no-sandbox")

    browser = webdriver.Chrome(options=option)
    browser.implicitly_wait(20)  # 隐式加载
    try:
        browser.get('https://weibo.com/')
        browser.maximize_window()
        # 等待微博登录框加载完成后输入账号密码登陆
        wb_locator = '.login_innerwrap .W_login_form[node-type=normal_form] input[name=username]'
        WebDriverWait(browser, 300, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, wb_locator)))
        browser.find_element_by_css_selector('.login_innerwrap [node-type=normal_form] input[name=username]').send_keys(
            username)
        browser.find_element_by_css_selector('.login_innerwrap [node-type=normal_form] input[name=password]').send_keys(
            password)
        # 增加延时
        time.sleep(3)

        # todo 验证码打码
        n = 0
        while True:
            sel = Selector(text=browser.page_source)
            verify_img = sel.css('[action-type=btn_change_verifycode]::attr(src)').get()
            if not verify_img:
                try:
                    browser.find_element_by_css_selector('.login_innerwrap [node-type=normal_form] .W_btn_a').click()
                except:
                    break
                break
            # if verify_img != 'about:blank' and n < 6:
            #     img_content = requests.get(verify_img).content
            #     # img = Image.open(BytesIO(img_content))
            #     # img.show()
            #     verify = verifycode(yundama, img_content)
            #     browser.find_element_by_css_selector('[value=验证码]').send_keys(verify)
            #     browser.find_element_by_css_selector('.login_innerwrap [node-type=normal_form] .W_btn_a').click()
            #     time.sleep(5)
            #     n += 1
            else:
                browser.find_element_by_css_selector('.login_innerwrap [node-type=normal_form] .W_btn_a').click()
                break

        # browser.find_element_by_css_selector('.login_innerwrap [node-type=normal_form] .W_btn_a').click()
        # 等待微博登陆完成后转到淘宝登陆页面并点击使用微博登陆
        wb_login_locator = '.WB_feed_detail'
        WebDriverWait(browser, 300, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, wb_login_locator)))
        browser.get('https://login.taobao.com')
        try:
            browser.find_element_by_css_selector('#J_Quick2Static').click()
        except Exception as e:
            print(f'错误信息{e}')
        browser.find_element_by_css_selector('.weibo-login').click()

        # 判断是否有微博快速登录框出现,有则点击,无则输入微博密码登陆
        if browser.find_element_by_css_selector('.logged_info .W_btn_g'):
            # tb_submit_locator = '.logged_info .W_btn_g'
            # WebDriverWait(browser, 300, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, tb_submit_locator)))
            browser.find_element_by_css_selector('.logged_info .W_btn_g').click()
        elif browser.find_elements_by_css_selector('[node-type=submitStates]'):
            return
            browser.find_element_by_css_selector('.enter_psw').send_keys(password)
            browser.find_element_by_css_selector('[node-type=submitStates]').click()

        # 等待淘宝登陆完成后转入淘宝m端首页
        tb_locator = '.logo-bd'
        WebDriverWait(browser, 300, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, tb_locator)))
        browser.get('https://h5.m.taobao.com')

        # 等待淘宝m端首页加载完成,获取cookie并存入redis
        m_tb_locator = '.header-bd'
        WebDriverWait(browser, 300, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, m_tb_locator)))
        cookies = browser.get_cookies()
        cookie = []
        nick = ''
        for item in cookies:
            cookie.append(item["name"] + "=" + item["value"])
            if item["name"] == '_nk_':
                nick = parse.unquote(item["value"])

        nick = json.loads(f'"{nick}"')
        cookiestr = ';'.join(item for item in cookie)

        # todo 为什么要存储在本地？
        # reds.hset('queue_cookie', nick, cookiestr)

        # todo 修改日志
        # cookie_info_logger.debug(f'{nick}: {cookiestr}')
        # time.sleep(100)
        browser.quit()

        # 本地
        url = 'http://127.0.0.1:8888/recieve_cookie'
        headers = {"Content-Type": "application/json"}
        data = {'data': {'cookie': cookiestr, 'nick': nick, "token": "ce934bc118beedabd789ed5cf6a20dc7"}}
        r = requests.post(url=url, headers=headers, json=data)
        # todo 增加日志
        print(r.status_code, r.json)

    except Exception as e:
        cookie_error_logger.error(f'cookie获取失败: {e}', exc_info=True)
    finally:
        browser.quit()
        # 下次获取cookies
        # 加入随机等待时间减少被反爬识别概率
        time.sleep(random.randint(1, 4))


def run():
    # todo 账号维护
    accounts = [
        {"username": 19181783661, "password": "puget123456"},
        {"username": 19181780307, "password": "puget123456"},
    ]
    for account in accounts:
        get_cookie(account)


if __name__ == '__main__':
    run()
