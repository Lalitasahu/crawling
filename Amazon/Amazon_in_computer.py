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
    'session-id': '257-2489097-8040666',
    'session-id-time': '2082758401l',
    'lc-acbin': 'en_IN',
    'csm-hit': 'tb:44F6T1BFYD1ZRBEMDE34+sa-2PTR606KC9RNVB8JFVSG-7DQYM86974P17033RVMG|1670729007285&t:1670729007285&adb:adblk_no',
    'ubid-acbin': '257-3146501-4312968',
    'x-acbin': '"?aCYESY@ulboVp?CV7GwtILVJhgWLVIfyZ?V7NVBhTe8BH3QtlTtzL27turSx@Q0"',
    'at-acbin': 'Atza|IwEBIAkpRBa9De701_JQeVipSlkEQTEOicwTnFLwbT390u9cvy2aR8eVX65ntoBFVVc0COeyMkfhgU6hrQw8Drs8rkRI_F8dcSxq5icYT89ueAZy1JaD7Um1O-Ugb31_8NilGqhMX5Qc3PhGU8jHg4jAdQkQlat2_T--M5FFpneXciDMEYLjC_j0v_G0hzu1QjKjnTN49Ev4cNcLNAH62BXYiF2C',
    'sess-at-acbin': '"vK5Fn8+fSULum75jsGEw4BmGCe+KwYcNqb20ay++DII="',
    'session-token': 'DVj1ZKTBQGgRBlSItMEkbZUXQ6xnIcTUVspjZktJ/NX6MbVAgOF5Pls5V2LTfIyWhUbjv1OEO4MJCXEm8ELmnMCAcpS9SLSAAjjfIgcayuCMlubF6/rvNPjB1nYwnmesnxfd4rlvdiq1gqHZI92D9QNYiTLS3jH8gK5ECgUSWkUso+Ivr1DZ2aIcDO0Uj2Npg4OEcMZYoyr4nAT8E4TpPXOdgNgfEttOsBAlYQLp6nsWqTzVhFGLBfYOyIyj3Ily',
    'i18n-prefs': 'INR',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'session-id=257-2489097-8040666; session-id-time=2082758401l; lc-acbin=en_IN; csm-hit=tb:44F6T1BFYD1ZRBEMDE34+sa-2PTR606KC9RNVB8JFVSG-7DQYM86974P17033RVMG|1670729007285&t:1670729007285&adb:adblk_no; ubid-acbin=257-3146501-4312968; x-acbin="?aCYESY@ulboVp?CV7GwtILVJhgWLVIfyZ?V7NVBhTe8BH3QtlTtzL27turSx@Q0"; at-acbin=Atza|IwEBIAkpRBa9De701_JQeVipSlkEQTEOicwTnFLwbT390u9cvy2aR8eVX65ntoBFVVc0COeyMkfhgU6hrQw8Drs8rkRI_F8dcSxq5icYT89ueAZy1JaD7Um1O-Ugb31_8NilGqhMX5Qc3PhGU8jHg4jAdQkQlat2_T--M5FFpneXciDMEYLjC_j0v_G0hzu1QjKjnTN49Ev4cNcLNAH62BXYiF2C; sess-at-acbin="vK5Fn8+fSULum75jsGEw4BmGCe+KwYcNqb20ay++DII="; session-token=DVj1ZKTBQGgRBlSItMEkbZUXQ6xnIcTUVspjZktJ/NX6MbVAgOF5Pls5V2LTfIyWhUbjv1OEO4MJCXEm8ELmnMCAcpS9SLSAAjjfIgcayuCMlubF6/rvNPjB1nYwnmesnxfd4rlvdiq1gqHZI92D9QNYiTLS3jH8gK5ECgUSWkUso+Ivr1DZ2aIcDO0Uj2Npg4OEcMZYoyr4nAT8E4TpPXOdgNgfEttOsBAlYQLp6nsWqTzVhFGLBfYOyIyj3Ily; i18n-prefs=INR',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'i': 'computers',
    'rh': 'n:1375392031',
    'fs': 'true',
    'page': '2',
    'qid': '1670728636',
    'ref': 'sr_pg_2',
}




# url  = 'https://www.amazon.de/-/en/s?i=computers&rh=n%3A427954031&fs=true&page=2&language=en&qid=1670602890&ref=sr_pg_{}'
alldata = []
for page in range(1,223):
    params['page'] = str(page)
    params['ref'] = str(page)
    # urls = url.format(page)
    response = requests.get('https://www.amazon.in/s', params=params, cookies=cookies, headers=headers)
    print(response.url)
    # r =  s.get(urls)
    tree = html.fromstring(response.text)
    products = tree.xpath('//div[@class="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"]')
    
    for product in range(len(products)):
        
            try:
                pro_link = 'https://www.amazon.in'+''.join(products[product].xpath('.//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]/@href'))
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
                'Category':'Desktop',
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
df.to_excel('amazon_desktop_in.xlsx',index=False)
print(alldata)