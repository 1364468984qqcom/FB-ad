# -*- coding: utf-8 -*-
import pandas as pd
from time import sleep
import re
import time
import tldextract
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import datetime
import yagmail
from multiprocessing import Pool

url_list = list()


def input_spu_return_Google_html(spu_word):
    url = 'https://www.google.com.hk/'
    res_list = []
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        sleep(.5)
        input = driver.find_element(By.NAME, 'q')
        input.send_keys(spu_word)
        sleep(.9)
        submit = driver.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
        submit.click()
        sleep(.5)
        res = driver.page_source

        res_list.append(res)
        while 1:
            try:
                next_page = driver.find_element(By.ID, 'pnnext')
                if next_page:
                    sleep(.5)
                    next_page.click()
                    response = driver.page_source
                    res_list.append(response)
                else:
                    driver.quit()

            except Exception:
                # driver.quit()
                break
    except Exception:
        input_spu_return_Google_html(spu_word)
    finally:
        return res_list


def input_spu_return_urlList():
    # url_list = list()
    global url_list
    # spu_word_list = ['SP0T1G1SPJC', 'Zins359F39963FDD', 'insF3BB913635D6', 'F32F029DA436']
    spu_word_list = pd.read_excel("D:\WorkProject\WorkProMail\参考产品10.25 FM.xlsx")['SPU ID'].to_list()
    spu_word_list_to_set = set(spu_word_list)
    spu_word_list = list(spu_word_list_to_set)
    for spu_word in spu_word_list:
        res_list = input_spu_return_Google_html(spu_word)
        for res in res_list:

            try:
                soup = BeautifulSoup(res, 'html.parser')
                div = soup.find(name='div', attrs={'id': 'rso'})
                a = div.find_all(name='a')
                a = a[0:len(a):2]
                for url in a:
                    url = str(url)
                    pattern = re.compile(r'href=(".*?")', re.S)
                    url = pattern.findall(url)
                    url = url[0]
                    if 'https://webcache.googleusercontent.com/' not in url and '/products/' in url and '//translate.google' not in url:
                        url_list.append(url)
            except Exception:
                pass
    url_list_to_set = set(url_list)
    url_list = [url.replace('"', '') for url in url_list_to_set]
    print(url_list)

    return url_list


def get_url_return_yuMing():
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ',
    }
    yuMing = list()
    url_list = input_spu_return_urlList()
    for url in url_list:
        try:
            spu_word = tldextract.extract(url).domain
            if spu_word:
                print(spu_word)
                yuMing.append(spu_word)
        except Exception as e:
            print(e)
    yuMing = set(yuMing)
    yuMing = list(yuMing)

    with open('YuMing.txt', 'a+', encoding='utf-8') as YuMingFile:
        for yu_ming in yuMing:
            YuMingFile.write(yu_ming)
            YuMingFile.write('\n')
    return yuMing
