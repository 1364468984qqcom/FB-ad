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


def input_yuMing_return_facebook_ad_num(key_word, fileName):
    global url_list
    facebook_url = "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=CN"
    driver = webdriver.Chrome()
    try:
        driver.get(facebook_url)
        sleep(1)
        input = driver.find_element(By.CLASS_NAME, '_7hgq')
        input.send_keys(key_word)
        sleep(1)
        try:
            button1 = driver.find_element(By.CSS_SELECTOR,
                                          '#content > div > div > div._7lcc._7pjc > div._7gaj > div > div._7gal > div > div > div._7hgv > div > button:nth-child(2) > div > div > div._7h1e._4ik4._4ik5')
            button1.click()
            # driver.refresh()
            sleep(.9)

            html = driver.page_source
            with open(fileName, 'a+', encoding='utf-8') as file:
                try:
                    try:
                        pattern = re.compile(r'<div .*?">([0-9 ]{0,} 条结果)</div></div></div>', re.S)
                        result = pattern.findall(html)[0]
                        print(result)
                    except Exception:
                        pattern = re.compile(r'<div .*?">([0-9 ]{0,}条结果)</div></div></div>', re.S)
                        result = pattern.findall(html)[0]
                        print(result)
                    local_time = datetime.now()
                    file.write(local_time.strftime("%Y-%m-%d  %H:%M:%S"))
                    file.write('              ')
                    file.write(key_word)
                    file.write('              ')
                    for url in url_list:
                        if key_word in url:
                            file.write(url)
                            break

                    file.write('     有')
                    file.write(result)
                    file.write('\n')
                except Exception:
                    pass
            # try:
            #     yag = yagmail.SMTP(user='13518160542@163.com', password='zjc123456', host='smtp.163.com')
            #     contents = ['发送Facebook广告数量的邮件']
            #     yag.send(['1364468984@qq.com', '728163448@qq.com'], '发送附件', contents, [fileName])
            # except Exception:
            #     yag = yagmail.SMTP(user='13518160542@163.com', password='zjc123456', host='smtp.163.com')
            #     contents = ['发送Facebook广告数量的邮件']
            #     yag.send(['1364468984@qq.com', '728163448@qq.com'], '发送附件', contents, [fileName])


        except IndexError:
            pass
        except Exception:
            pass



    except Exception:
        input_yuMing_return_facebook_ad_num(key_word, fileName)
    finally:
        sleep(.5)
        driver.quit()


def input_one_key_word_to_facebook(fileName):
    strat_time = time.time()
    yuMing = get_url_return_yuMing()
    for key_word in yuMing:
        input_yuMing_return_facebook_ad_num(key_word, fileName)
    end_time = time.time()
    print('运行时间为:{}'.format(end_time - strat_time))


if __name__ == '__main__':
    now_time = time.strftime("%Y-%m-%d__%H-%M-%S", time.localtime(time.time()))
    fileName = "D:\WorkProject\CrawlPro\Get_FB_ad_Data\Test" + '\\' + now_time + r'.txt'
    print(fileName)

    # pool = Pool(6)
    # for i in range(3):
    #     pool.apply_async(input_spu_return_Google_html, args=(spu_word,))
    # pool.close()
    # pool.join()
    # pool.map(input_one_key_word_to_facebook, fileName)

    input_one_key_word_to_facebook(fileName)
