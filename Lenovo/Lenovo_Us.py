import re
import json
import requests
import pandas as pd
from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html
import concurrent.futures
s = Session()
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"

alldata = []
def listpage():
    url = 'https://www.lenovo.com/us/en/laptops/subseries-results?visibleDatas=993:Everyday%20Use'
    urlapi = 'https://openapi.lenovo.com/us/en/ofp/search/dlp/product/query/get/_tsc?pageFilterId=a7b024c8-a164-4c56-b65e-0c20fe323ada&subSeriesCode=&params=%7B%22classificationGroupIds%22%3A%22400001%22%2C%22pageFilterId%22%3A%22a7b024c8-a164-4c56-b65e-0c20fe323ada%22%2C%22facets%22%3A%5B%7B%22facetId%22%3A%22993%22%2C%22selectedValues%22%3A%22Everyday%20Use%22%7D%5D%2C%22page%22%3A%221%22%2C%22pageSize%22%3A20%2C%22init%22%3Atrue%2C%22sorts%22%3A%5B%22bestSelling%22%5D%2C%22version%22%3A%22v2%22%2C%22subseriesCode%22%3A%22%22%7D'
    r = s.get(urlapi)
    js = r.json()
    products =  js['data']['data'][0]['products']
    # print(products.keys())
    for product in range(len(products)):
        id = products[product].get('id')
        name = products[product].get('productName')
        pro_url = 'https://www.lenovo.com/us/en'+products[product].get('url')
        pro_code = products[product].get('productCode')
        price = products[product].get('miniPrice')
        ratingStar = products[product].get('ratingStar')
        commentCount = products[product].get('commentCount')
        marketingShortDescription = bs(products[product].get('marketingShortDescription')).text
        image = 'https:'+products[product].get('media').get('listImage')[0].get('imageAddress')
        # print(image)
        data ={
            'landingPage':url,
            'product_rank': product,
            'id':id,
            'name':name,
            'pro_url':pro_url,
            'pro_code':pro_code,
            'price':price,
            'ratingStar':ratingStar,
            'commentCount':commentCount,
            'marketingShortDescription':marketingShortDescription,
            'image':image
            
        }
        alldata.append(data)
        print(data)
listpage()
df = pd.DataFrame(alldata)
df.to_excel('lenovo_us_everdayuse_laptop.xlsx',index=False)