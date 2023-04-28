from requests import Session
from lxml import html
import json, re
import pandas as pd
from bs4 import BeautifulSoup as BS
from scrapingbee import ScrapingBeeClient
import concurrent.futures
s = Session()
c = ScrapingBeeClient(api_key='DE592OF1RHAFV3P69R2G2127NVVFJ4RGGG159ST4X2Y0TTPYDTA9J4OKZ74E0AN4X9ZUKSUS12GC3O04')
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"

def listpage():
    page = 1
    url = 'https://www.lenovo.com/gb/en/laptops/subseries-results/?visibleDatas=2769%3ATraditional%20Laptops' 
    api = f'https://openapi.lenovo.com/gb/en/ofp/search/dlp/product/query/get/_tsc?pageFilterId=f1781e40-36a9-47bc-a636-6e21e05aca1f&subSeriesCode=&params=%7B%22classificationGroupIds%22%3A%22400001%22%2C%22pageFilterId%22%3A%22f1781e40-36a9-47bc-a636-6e21e05aca1f%22%2C%22facets%22%3A%5B%7B%22facetId%22%3A%222769%22%2C%22selectedValues%22%3A%22Traditional%20Laptops%22%7D%5D%2C%22page%22%3A1%2C%22pageSize%22%3A20%2C%22init%22%3Atrue%2C%22sorts%22%3A%5B%22newest%22%5D%2C%22version%22%3A%22v2%22%2C%22subseriesCode%22%3A%22%22%7D'
    # r = s.get(api)
    r = c.get(api,params= {'render_js':False,'wait':5000,'premium_proxy': True,'country_code':'gb',"block_resources":False})
    js = r.json()
    # products = 
    print(js)

listpage()