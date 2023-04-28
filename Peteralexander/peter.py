import requests 
from bs4 import BeautifulSoup as bs
from requests import Session
import pandas as pd 
import math
import re
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

all = []
def crwal_list():
    pageSize = 48
    nextpage = True
    while nextpage:
        api = f'https://www.peteralexander.com.au/shop/ProductListingViewV2?jspStoreDir=PeterAuroraStorefrontAssetStore&doLazyLoad=true&urlLangId=-1&enableSKUListView=false&pgl_widgetSlotId=6&catalogId=20101&contentNames=&resultsPerPage=48&searchTerm=&fromRefinement=true&resizeTo=?i10c=img.resize(width:6)&pgl_widgetDefId=-3011&fromPage=catalogEntryList&top_category=333052&sortBy=0&resultType=products&pgl_widgetId=3074457345618276177&pageGroup=Category&storeId=20101&pageView=grid&beginIndex=0&emsName=Widget_CatalogEntryList_801_3074457345618276177&includedSearchSetup=ajaxincludedSearchSetup&langId=-1&contentPositions=&categoryId=352071&parent_category_rn=333052&pageSize={pageSize}'
        r = s.get(api)
        print(r,r.url)
        soup = bs(r.text,'html.parser')
        count = re.search('totalCount:(.*?),',r.text).group(1)
        if pageSize <= int(count):
        
            products = soup.find_all('div',"product product__item")
            for product in products:
                Name = product.find('div','product__name').text.strip()
                data = {
                    'Name':Name
                }
                all.append(data)
                print(data)
        else:
            break
        pageSize += 48
crwal_list()
