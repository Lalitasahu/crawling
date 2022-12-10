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
    'session-id-time': '2082787201l',
    'i18n-prefs': 'EUR',
    'lc-acbde': 'en_GB',
    'sp-cdn': '"L5Z9:IN"',
    'csm-hit': 'tb:FBRYWFMRHC318QKB1J76+s-0TRVX5MJNMCPS3492T1X|1670668894999&t:1670668894999&adb:adblk_no',
    'ubid-acbde': '258-3279326-7357765',
    'session-token': '"15D5SnKzHF72G/xAwubFiGC0juLaAa98s5a0YuXC9kW53LyUj90nTOCp+m8TJCzgtToYayH5NZF/twv9SLHekYzwMfnr+hp9Tcn+CYVu7Dj/bTjxtlaQQlFARTyBWereNePKJMzIHAYyN4t+x3khd6vLHuZAUmXcE5Bz7Ohk00n1zNy02Hqdm+tCETFX4bOXBy7WJaMyZ6aO+y0qyXPkiTwuygMWI5CtW/RjJD4EZcc="',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'session-id=262-8014393-4805925; session-id-time=2082787201l; i18n-prefs=EUR; lc-acbde=en_GB; sp-cdn="L5Z9:IN"; csm-hit=tb:FBRYWFMRHC318QKB1J76+s-0TRVX5MJNMCPS3492T1X|1670668894999&t:1670668894999&adb:adblk_no; ubid-acbde=258-3279326-7357765; session-token="15D5SnKzHF72G/xAwubFiGC0juLaAa98s5a0YuXC9kW53LyUj90nTOCp+m8TJCzgtToYayH5NZF/twv9SLHekYzwMfnr+hp9Tcn+CYVu7Dj/bTjxtlaQQlFARTyBWereNePKJMzIHAYyN4t+x3khd6vLHuZAUmXcE5Bz7Ohk00n1zNy02Hqdm+tCETFX4bOXBy7WJaMyZ6aO+y0qyXPkiTwuygMWI5CtW/RjJD4EZcc="',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}

params = {
    'i': 'computers',
    'rh': 'n:427954031',
    'fs': 'true',
    'page': '2',
    'language': 'en',
    'qid': '1670602890',
    'ref': 'sr_pg_1',
}


# url  = 'https://www.amazon.de/-/en/s?i=computers&rh=n%3A427954031&fs=true&page=2&language=en&qid=1670602890&ref=sr_pg_{}'
alldata = []
for page in range(1,40):
    params['page'] = str(page)
    params['ref'] = str(page)
    # urls = url.format(page)
    response = requests.get('https://www.amazon.de/s', params=params, cookies=cookies, headers=headers)
    print(response.url)
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
                'landingpageUrl':response.url,
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
df.to_excel('amazon_desktop.xlsx',index=False)
print(alldata)