import re
import json
import requests
import pandas as pd
from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html
s = Session()
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"

cookies = {
    'session-id': '262-8014393-4805925',
    'session-id-time': '2082754801l',
    'i18n-prefs': 'EUR',
    'lc-acbde': 'en_GB',
    'sp-cdn': '"L5Z9:IN"',
    'csm-hit': 'tb:MCTFP639TWC3EHWQZ5ER+s-48F2C7T744PKKF899292|1670673714157&t:1670673714158&adb:adblk_no',
    'ubid-acbde': '258-3279326-7357765',
    'session-token': '"VYh/GVzkUJEsV8B7kkBWQl3ger2p3y7e6f/MZkXlpdb2+/cko+/rSIo1Z15WfIB6zcZhkVqN3GsL9yyI+fXguBrdYfWSCh8S9DyMwocAgme33FzLeYWRTojeW2Uc96ps+8vEUOLtvzyLfVgbLPNVmE70nl2DHajmrk9YSy07h9Ojv3fCS+/EhokJYLGEJelwujtB+kOx8s8jpei8ZP8902Lh7+pGveiBUuo5+V0zxLk="',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'session-id=262-8014393-4805925; session-id-time=2082754801l; i18n-prefs=EUR; lc-acbde=en_GB; sp-cdn="L5Z9:IN"; csm-hit=tb:MCTFP639TWC3EHWQZ5ER+s-48F2C7T744PKKF899292|1670673714157&t:1670673714158&adb:adblk_no; ubid-acbde=258-3279326-7357765; session-token="VYh/GVzkUJEsV8B7kkBWQl3ger2p3y7e6f/MZkXlpdb2+/cko+/rSIo1Z15WfIB6zcZhkVqN3GsL9yyI+fXguBrdYfWSCh8S9DyMwocAgme33FzLeYWRTojeW2Uc96ps+8vEUOLtvzyLfVgbLPNVmE70nl2DHajmrk9YSy07h9Ojv3fCS+/EhokJYLGEJelwujtB+kOx8s8jpei8ZP8902Lh7+pGveiBUuo5+V0zxLk="',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'i': 'computers',
    'rh': 'n:427957031',
    'fs': 'true',
    'page': '1',
}


url  = 'https://www.amazon.de/s?i=computers&rh=n%3A427957031&fs=true&page={}'
alldata = []
for page in range(1,401):
    urls = url.format(page)
    print(urls)
    response = requests.get('https://www.amazon.de/s', params=params, cookies=cookies, headers=headers)
    # r =  s.get(urls)
    tree = html.fromstring(response.text)
    products = tree.xpath('//div[@class="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"]')
    
    for product in range(len(products)):
        
            try:
                pro_link = 'https://www.amazon.de'+''.join(products[product].xpath('.//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]/@href'))
            except:
                pro_link = ''
            try:
                product_id = pro_link.split('/dp/')[-1].split('/')[0]
            except:
                product_id = ''
            try:
                titel = ''.join(products[product].xpath('.//span[@class="a-size-base-plus a-color-base a-text-normal"]//text()'))
            except:
                titel =''
            try:
                price = ''.join(products[product].xpath('.//span[@class="a-offscreen"]//text()'))
            except:
                price =''
            try:
                Image= ''.join(products[product].xpath('.//div[@class="a-section aok-relative s-image-square-aspect"]//img/@src'))
            except:
                Image = ''
            try:
                Review = ''.join(products[product].xpath('.//span[@class="a-size-base s-underline-text"]//text()'))
            except:
                Review = ''
            try:
                Rating = ''.join(products[product].xpath('.//span[@class="a-icon-alt"]//text()'))
            except:
                Rating = ''
            # product = product.xpath('//text()')
            data = {
                'landingpageUrl':urls,
                'pro_link':pro_link,
                'Product_id':product_id,
                'S1_Titel':titel,
                'S2_image':Image,
                'price':price,
                'Review':Review,
                'Rating':Rating,
                'page_rank':page,
                'Product_rank':product
                # 'product_count': product
            }
            alldata.append(data)

df = pd.DataFrame(alldata)
df.to_excel('amazon_laptop.xlsx',index=False)
print(alldata)