import requests
import re
import json
import csv
import time
import pandas as pd
from requests import Session
from bs4 import BeautifulSoup as bs
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

xl=csv.writer(open('Peteralexander.csv','w',newline=''))
xl.writerow(['Name','product_link','image','off','color','Details','Care_For_Me','Delivery'])


def crwal_detail(url):
    r = s.get(url)
    soup = bs(r.text, 'html.parser')    

    try:
        off = soup.find('span','afterpay__message').text.replace('\r','').replace('\t','').replace('\n','')
    except:
        off = ''


    try:
        color = re.search('"colour":"(.*?)"',r.text).group(1)
    except:
        color = " "

    info = json.loads(json.loads(re.search('"description" : (.*?)}",',r.text).group(1)+'}"'))         
    Details = info['PD'].replace('&lt;','').replace('p&gt;','').replace('/li&gt;','').replace('li&gt;','').replace('/ul&gt;','')
    Care_For_Me = info['FC'].replace('&lt;','').replace('p&gt;','').replace('/li&gt;','').replace('li&gt;','').replace('/ul&gt;','')
    try:
        Delivery =  soup.find('div',{'id':'STATIC'}).text.strip()
    except:
        Delivery = ' '
        
    data = {
        'off':off,
        'color':color,
        'Details':Details,
        'Care_For_Me':Care_For_Me,
        'Delivery':Delivery
    }
    return data



alldata = []
def crwal_list():
    r = s.get(url)
    time.sleep(3)
    soup = bs(r.text,'html.parser')
    pageSize = 48
    nextpage = True
    while nextpage:
        api = f'https://www.peteralexander.com.au/shop/ProductListingViewV2?jspStoreDir=PeterAuroraStorefrontAssetStore&doLazyLoad=true&urlLangId=-1&enableSKUListView=false&pgl_widgetSlotId=6&catalogId=20101&contentNames=&resultsPerPage=48&searchTerm=&fromRefinement=true&resizeTo=?i10c=img.resize(width:6)&pgl_widgetDefId=-3011&fromPage=catalogEntryList&top_category=333052&sortBy=0&resultType=products&pgl_widgetId=3074457345618276177&pageGroup=Category&storeId=20101&pageView=grid&beginIndex=0&emsName=Widget_CatalogEntryList_801_3074457345618276177&includedSearchSetup=ajaxincludedSearchSetup&langId=-1&contentPositions=&categoryId=352071&parent_category_rn=333052&pageSize={pageSize}'
        r = s.get(api)
        print(r,r.url)
        soup = bs(r.text,'html.parser')
        count = re.search('totalCount:(.*?),',r.text).group(1)
        if pageSize < int(count):
            products = soup.find_all('div',"product product__item")
            for product in products:
                try:
                    Name = product.find('div','product__name').text.strip()
                except:
                    Name = ''
                try:
                    product_link = product.find('a','product__item--image').get('href')
                except:
                    product_link = ''
                # price = re.search('"listPrice" :"(.*?)",',r.text).group(1)
                try:
                    image = 'https://www.peteralexander.com.au'+product.find('figure').find('img').get('src')
                except:
                    image = ''
                try:
                    detail = crwal_detail(product_link)
                except:
                    detail = ''

                # print(img)
                datas = {
                    'Name':Name,
                    'product_link':product_link,
                    # 'price':price,
                    'image':image
                }
                datas.update(detail)
                alldata.append(datas)
                xl.writerow(datas.values())
                print(datas)
        else:
            break
        pageSize += 48
url = 'https://www.peteralexander.com.au/shop/en/peteralexander/all-new'
crwal_list()

df = pd.DataFrame(alldata)
df.to_excel('petera.xlsx',index=False)



