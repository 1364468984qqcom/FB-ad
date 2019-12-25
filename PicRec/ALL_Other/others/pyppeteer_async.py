from pyppeteer import launch
import asyncio


async def main1():
    url = 'http://quotes.toscrape.com/js/'
    brower = await launch(headless=False)  #headless=False为开启界面浏览器，不写即为默认的无界面浏览器
    page = await brower.newPage()
    await page.goto(url)
    await page.screenshot(path='baidu21.png')
    await page.pdf(path='baidu21.pdf')
    dimensions = await page.evaluate('''() => {
           return {
               width: document.documentElement.clientWidth,
               height: document.documentElement.clientHeight,
               deviceScaleFactor: window.devicePixelRatio,
           }
       }''')
    print(dimensions)  # {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    # await asyncio.sleep(4)

    await brower.close()


# asyncio.get_event_loop().run_until_complete(main())
import time

s = time.time()
asyncio.get_event_loop().run_until_complete(main1())
e = time.time()
print(e-s)

# asyncio.get_event_loop().run_until_complete(main1())