from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import pymongo
import time
import datetime

import re
import multiprocessing

import lxml.html
import lxml.etree

# ---------- 1. 一些配置信息  ------------
# 搜索关键字列表
keySearchWords = {
    "动漫": [1, "动漫周边"],
    "水果": [1, "水果沙拉"],
}

# 数据库初始化
# client = pymongo.MongoClient("127.0.0.1:27017")
# db = client["taobao"]
# db_coll = db["productInfo"]

# 一个页面的最大重试次数
retryMax = 8

chrome_options = webdriver.ChromeOptions()


# 禁止图片和视频的加载，提高网页爬取速度
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_options.add_experimental_option("prefs", prefs)

# 启用headless模式：无浏览器界面，提高速度与稳定性
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')


# ---------- 2. 解析页面信息  ------------
# 获得每个产品在list页面的主要信息

def getProductMainInfo(htmlSource):
    try:
        resultTree = lxml.etree.HTML(htmlSource)
        # fix_html = lxml.html.tostring(resultTree, pretty_print=True)
        # print(f"htmlSource = {htmlSource}")

        productLst = resultTree.xpath("//div[@class='m-itemlist']//div[contains(@class, 'J_MouserOnverReq')]")
        print(f"productLst = {productLst}")
        productInfoLst = []
        for product in productLst:
            productInfo = {}

            # 唯一标记
            dataNid = product.xpath(".//div[contains(@class,'ctx-box')]//div[contains(@class, 'title')]/a/@data-nid")
            if len(dataNid) > 0:
                productInfo['dataNid'] = dataNid[0]
            else:
                productInfo['dataNid'] = 0
            productInfo['_id'] = productInfo['dataNid']

            taobaoCategory = product.xpath("@data-category")
            if len(taobaoCategory) > 0:
                productInfo['taobaoCategory'] = taobaoCategory[0]
            else:
                productInfo['taobaoCategory'] = 'unknow'

            rank = product.xpath("@data-index")
            if len(rank) > 0:
                productInfo['rank'] = rank[0]
            else:
                productInfo['rank'] = 0

            imgSrc = product.xpath(".//div[@class='pic']/a//img/@src")
            if len(imgSrc) > 0:
                productInfo['imgSrc'] = imgSrc[0]
            else:
                productInfo['imgSrc'] = ''

            title = product.xpath(".//div[contains(@class,'ctx-box')]//div[contains(@class, 'title')]/a/text()")
            productInfo['title'] = ''
            if len(title) > 0:
                for elem in title:
                    productInfo['title'] += elem.strip()

            detailUrl = product.xpath(".//div[contains(@class,'title')]//a/@href")
            if len(detailUrl) > 0:
                productInfo['detailUrl'] = detailUrl[0]
            else:
                productInfo['detailUrl'] = ''

            shopName = product.xpath(
                ".//div[contains(@class,'ctx-box')]//div[@class='shop']/a[contains(@class,'shopname')]/span/text()")
            if len(shopName) > 0:
                productInfo['shopName'] = shopName[-1]
            else:
                productInfo['shopName'] = ''

            shopHref = product.xpath(
                ".//div[contains(@class,'ctx-box')]//div[@class='shop']/a[contains(@class,'shopname')]/@href")
            if len(shopHref) > 0:
                productInfo['shopHref'] = shopHref[0]
            else:
                productInfo['shopHref'] = ''
            print(f"shopHref = {shopHref}")

            shopID = product.xpath(
                ".//div[contains(@class,'ctx-box')]//div[@class='shop']/a[contains(@class,'shopname')]/@data-userid")
            if len(shopID) > 0:
                productInfo['shopID'] = shopID[0]
            else:
                productInfo['shopID'] = ''
            print(f"shopID = {shopID}")

            location = product.xpath(".//div[contains(@class,'clearfix')]//div[@class='location']/text()")
            if len(location) > 0:
                productInfo['location'] = location[0]
            else:
                productInfo['location'] = ''

            dealCountRes = product.xpath(".//div[contains(@class,'ctx-box')]//div[@class='deal-cnt']/text()")
            if len(dealCountRes) > 0:
                dealCount = dealCountRes[0]
                if dealCount != '':
                    dealCountRe = re.search('(\d+)', dealCount)
                    dealCount = int(dealCountRe.group(1)) if dealCountRe else 0.0
                    productInfo['dealCount'] = dealCount
            else:
                productInfo['dealCount'] = 0

            # 价格放到了 <span class="sm-offer-priceNum sw-dpl-offer-priceNum" title="¥6.60">
            # productInfo['price'] = product.xpath(".//span[contains(@class,'priceNum')]//text()")
            price = product.xpath(".//div[contains(@class,'price')]//strong/text()")
            if len(price) > 0:
                price = price[0]
            else:
                price = ''
            if price != '':
                # 处理价格：price = ￥64.32'
                priceRe = re.search(r'([\d\.]+)', price)
                priceFloat = float(priceRe.group(1)) if priceRe else 0.0
                productInfo['price'] = priceFloat
            else:
                productInfo['price'] = 0.0

            print(f"productInfo = {productInfo}")
            productInfoLst.append(productInfo)
        return productInfoLst
    except Exception as e:
        print(f"解析List 商品信息出错，e = {e}")
        return []


# 第一步，进入首页，搜索关键字
def searchKey(browser, wait, keyWord, categorySearchWords, retryCount):
    print(
        f"searchKey: enter, keyWord = {keyWord}, categorySearchWords = {categorySearchWords}, retryCount = {retryCount}")
    retryCount += 1
    if retryCount > retryMax:
        return (False, 0, keyWord)
    mainUrl = "https://www.taobao.com/"
    print(f"searchKey: 访问taobao主页, 进行搜索. mainUrl = {mainUrl}")
    browser.get(mainUrl)

    # 尝试搜索
    try:
        # 搜索框是否出现
        input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='search-combobox-input']"))
        )
    except Exception as e:
        # 搜索框都没出现，说明页面没有加载好，重试
        print(f"searchKey: 搜索框还没有加载好，重新加载主页. retryCount = {retryCount}, url = {mainUrl}, e = {e}")
        searchKey(browser, wait, keyWord, categorySearchWords, retryCount)
    else:
        try:
            # 重新拿到搜索框，防止页面在这个时间有变化，导致input元素失焦
            input = browser.find_element_by_xpath("//input[@class='search-combobox-input']")
            # 输入搜索关键字
            time.sleep(3)
            input.clear()
            input.send_keys(categorySearchWords)
            # 敲enter键
            input.send_keys(Keys.RETURN)
            print(f"searchKey: press return key.")
            time.sleep(3)

            # 查看搜索结果是否出现
            searchRes = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='m-itemlist']"))
            )
            print(f"searchKey: searchSuccess, searchRes = {searchRes}")
        except Exception as e:
            print(f"searchKey: 搜索结果总页数尚未加载好，重新加载主页. retryCount = {retryCount}, url = {mainUrl}, e = {e}")
            searchKey(browser, wait, keyWord, categorySearchWords, retryCount)
        else:
            # 如果发现结果页加载OK, 开始寻找总页数
            try:
                # 获取结果总页数
                print(f"searchKey: 搜索结果已出现，开始寻找总页数")
                totalPage = 0
                print(f"searchKey: totalPageInit = {totalPage}")
                #  共 100 页，
                totalRes = wait.until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='total']"))
                )
                # print(f"totalRes.text = {totalRes.text}")
                totalRe = re.search("(\d+)", totalRes.text)
                # print(f"totalRe = {totalRe}")
                totalPage = int(totalRe.group(1))
                print(f"searchKey: totalPage = {totalPage}")
                return (True, totalPage, keyWord)
            except Exception as e:
                print(f"searchKey: 搜索结果就一页. e = {e}")
                return (True, 1, keyWord)
            finally:
                # 这个部分会在本函数return语句之前执行
                # 参考文章：Python :浅析 return 和 finally 共同挖的坑
                # http://python.jobbole.com/88408/
                try:
                    print(f"searchKey: 取第一页的数据出来，进行存储")
                    # 解析页面内容：
                    if browser.page_source:
                        productInfoLst = getProductMainInfo(browser.page_source)
                        for product in productInfoLst:
                            product['item_type'] = "productMainInfo"
                            product['keyWord'] = keyWord
                            product['page'] = 1
                            product['markClawerTools'] = 1
                            product['reverse1'] = 1
                            product['categorySearchWords'] = categorySearchWords
                            try:
                                insertRes = db_coll.insert_one(product)
                                print(f"searchKey: insertRes = {insertRes.inserted_id}")
                            except Exception as e:
                                print(f"searchKey: insert_one Exception = {e}")
                except Exception as e:
                    print(f"searchKey: 取第一页数据出来这个过程出现异常。Exception = {e}")


# 输入页码，然后点击按钮，进行翻页
def getNextListPage(browser, wait, pageNum, retryCount):
    print(f"getNextListPage: enter, pageNum = {pageNum}, retryCount = {retryCount}")
    retryCount += 1
    if retryCount > retryMax:
        return (False, [])

    # 第一步判断List页是否加载成功，看一下下面的页码输入框是否加载好了
    try:
        input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='form']/input[@class='input J_Input']"))
        )
    except Exception as e:
        # 刷新当前页面，然后重新查看数据
        print(f"getNextListPage: 页码输入框尚未加载好，刷新当前页面，循环这个过程. retryCount = {retryCount}")
        browser.refresh()
        time.sleep(2)
        getNextListPage(browser, wait, pageNum, retryCount)
    else:
        # 开始输入页码数，进行翻页
        try:
            # 重新获取输入框，防止原先获取的input元素失焦
            input = browser.find_element_by_xpath("//div[@class='form']/input[@class='input J_Input']")
            input.clear()
            input.send_keys(pageNum)
            submit = browser.find_element_by_xpath("//div[@class='form']/span[@class='btn J_Submit']")
            submit.click()
            # 检查下面高亮的页码数和这次输入的是否一致，也就是说是否翻页成功
            activePage = wait.until(
                EC.text_to_be_present_in_element((By.XPATH, "//ul[@class='items']/li[@class='item active']/span"),
                                                 str(pageNum))
            )
            # 检测翻页后商品列表是否加载成功
            allProducts = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='m-itemlist']"))
            )
            # 解析页面内容：
            if browser.page_source:
                productInfoLst = getProductMainInfo(browser.page_source)
                return (True, productInfoLst)
            else:
                # 如果获取不到源代码，说明页面加载出错，刷新，重新获取
                browser.refresh()
                time.sleep(2)
                getNextListPage(browser, wait, pageNum, retryCount)
        except Exception as e:
            print(f"getNextListPage: 无法解析当前页列表下的商品，重新刷新，pageNum = {pageNum}, retryCount = {retryCount}, e = {e}")
            browser.refresh()
            time.sleep(2)
            getNextListPage(browser, wait, pageNum, retryCount)


# 浏览器进程，多进程执行单位，爬取淘宝数据主要流程...
def chromeProcessPer(queue, lock, mark):
    clawerStartTime = datetime.datetime.now()
    print(f"chromeProcessPer enter: clawerMark = {mark}, time = {clawerStartTime}")

    # 启动浏览器，并设置好wait
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.set_window_size(900, 900)  # 根据桌面分辨率来定，主要是为了抓到验证码的截屏
    wait = WebDriverWait(browser, timeout=30)

    # 从队列中获取搜索关键字
    while not queue.empty():
        keyWordInfo = queue.get()

        # 加锁，是为了防止散乱的打印。 保护一些临界状态
        # 多个进程运行的状态下，如果同一时刻都调用到print，那么显示的打印结果将会混乱
        lock.acquire()
        # keyWordInProcess = ('动漫', [1, '动漫周边']), markProcess = 1
        print(f"keyWordInProcess = {keyWordInfo}, markProcess = {mark}")
        lock.release()
        time.sleep(1)

        # 按照品类的搜索关键字来搜索
        searchRes = searchKey(browser, wait, keyWordInfo[0], keyWordInfo[1][1], 0)
        print(f"main: searchRes = {searchRes}, clawerMark = {mark}")
        if ((searchRes != None)) and searchRes[0] == True:
            # 从第二页开始存储，因为有的商品可能就一页，在搜索结果中就处理掉了。 而且也没有页码输入框，无法与下面的流程匹配
            if searchRes[1] > 1:
                for page in range(2, searchRes[1] + 1):
                    # time.sleep(5)      # 根据淘宝反爬策略调整延时
                    listPageRes = getNextListPage(browser, wait, page, 0)
                    print(
                        f"chromeProcesser: keyWord = {keyWordInfo}, page = {page}, listPageRes = {listPageRes},  mark = {mark}")
                    if (listPageRes != None) and (listPageRes[0] == True):
                        for product in listPageRes[1]:
                            product['item_type'] = "productMainInfo"
                            product['keyWord'] = keyWordInfo[0]
                            product['page'] = page
                            product['markClawerTools'] = 1
                            product['reverse1'] = 1
                            product['categorySearchWords'] = keyWordInfo[1][1]
                            # try:
                            #     insertRes = db_coll.insert_one(product)
                            #     print(f"insertRes = {insertRes.inserted_id}")
                            # except Exception as e:
                            #     print(f"insert_one Exception = {e}")
            else:
                print(f"main: keyWord = {keyWordInfo}, totalPage = {searchRes[1]}, clawerMark = {mark}")
    clawerEndTime = datetime.datetime.now()
    # 一定要退出
    browser.quit()
    print(
        f"chromeProcessPer end: clawerMark = {mark}, time = {clawerEndTime}, timeUsed = {clawerEndTime - clawerStartTime}")


if __name__ == "__main__":
    mainStartTime = datetime.datetime.now()
    print(f"main: taobao mainStartTime = {mainStartTime}")

    lock = multiprocessing.Lock()  # 进程锁
    queue = multiprocessing.Queue(300)  # 队列，用于存放所有的初始关键字，最大为300个

    for keyWord, keyWordValue in keySearchWords.items():
        print(f"keyWord = {keyWord}, keyWordValue = {keyWordValue}")
        # 如果queue定的太小，剩下的放不进去，程序就会block住，等待队列有空余空间
        # def put(self, obj, block=True, timeout=None):
        queue.put((keyWord, keyWordValue))
    print(f"queueBefore = {queue}")

    getKeyProcessLst = []
    # 生成两个进程，并启动
    for i in range(2):
        # 携带的args 必须是python原有的数据类型，不能是自定义的。否则lock锁不住该对象
        process = multiprocessing.Process(target=chromeProcessPer, args=(queue, lock, i))
        process.start()
        getKeyProcessLst.append(process)

    # 守护线程
    # join 等待线程终止，如果不使用join方法对每个线程做等待终止，那么线程在运行过程中，可能会去执行最后的打印
    # 如果没有join，父进程就不会阻塞，启动子进程之后，父进程就直接执行最后的打印了
    for p in getKeyProcessLst:
        p.join()

    print(f"queueAfter = {queue}")
    queue.close()
    print(f"all queue used.")
    mainEndTime = datetime.datetime.now()
    print(
        f"### timeUsedTotal = {mainEndTime - mainStartTime}, mainStartTime = {mainStartTime}, mainEndTime = {mainEndTime}")
