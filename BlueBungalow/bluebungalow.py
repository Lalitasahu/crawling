import requests 
import time 
import csv
from requests import Session
from bs4 import BeautifulSoup as bs
import pandas as pd
import concurrent.futures

s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

xl=csv.writer(open('bluebungalow.csv','w',newline='', encoding='utf-8'))
xl.writerow(['landingPage','main_api_url','pro_id','link','title','brand','date','availability','price','imageList','description','Shipping_Returns'])

def detailpage(row):
    r = s.get(row['link'])
    description = ''
    Shipping_Returns = ''
    soup = bs(r.text, 'html.parser')
    try:
        for i in soup.find('div','product-tabs-content-inner clearfix').find_all('li'):
            description = i.text
    except:
            description = ''
    try:
        Shipping_Returns = soup.find('div','panel panel-default panel-custom-tab').find('div','product-tabs-content-inner clearfix').text.strip()
    except:
        Shipping_Returns = ''
    deta ={
        'description':description,
        'Shipping_Returns':Shipping_Returns,
    }
    deta.update(row)
    products.append(deta)
    print(deta)


def listpage(url):
    url = row['SubUrl']
    url_id = url.split('/')[-1]
    start = 0
    nextpage = True
    while nextpage:
        url = f'https://search.unbxd.io/ac541912a18c803bfeab27f04ccbebf4/prod-bluebungalow-au4941591590495/category?&rows=30&start={start}&p=categoryPath%3A%22{url_id}%22&format=json&view=grid&stats=price&fields=title,uniqueId,collection_tag,plain_tags,publishedAt,secondaryImageUrl,documentType,imageUrl,price,sellingPrice,priceMax,sku,imageUrl,sizeMap,relevantDocument,productUrl,variantId,brand,availability,altImageUrl,altImageTag,imageList&facet.multiselect=true&pagetype=boolean&version=V2&indent=off&filter=documentType:product&filter=publishedAt:*&device-type=Desktop&unbxd-url=https%3A%2F%2Fbluebungalow.com.au%2Fcollections%2F{url_id}&unbxd-referrer=&user-type=new&api-key=ac541912a18c803bfeab27f04ccbebf4'
        # time.sleep(3)
        r = s.get(url)
        js = r.json()
        products = js['response']['products']
        if products:
            for product in products:
                pro_id = product.get('uniqueId')
                link = 'https://bluebungalow.com.au'+product.get('productUrl')
                title = product.get('title')
                brand = ''.join(product.get('brand'))                
                date = product.get('publishedAt')
                availability = product.get('availability')
                price = product.get('price')
                # sellingPrice = product.get('sellingPrice')
                imageList = product.get('imageList')
                # detail = detailpage(link)


                data = {
                    'landingPage':row['SubUrl'],
                    'main_api_url':url,
                    'pro_id':pro_id,
                    'link':link,
                    'title':title,
                    'brand':brand,
                    'date':date,
                    'availability':availability,
                    'price':price,
                    'imageList':imageList
                }
                # data.update(detail)
                print(data)
                alldata.append(data)
                xl.writerow(data.values())
        else:
            break
        print(start)
        start += 30


alldata = []
products = []
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#     df = pd.read_excel('bluebungalow_cat_Url.xlsx')
#     for i in range(len(df)):
#     # for i in range(3):
#         row = df.iloc[i].to_dict()
#         # listpage(row)
#         executor.submit(listpage,row)


# df = pd.DataFrame(alldata)
# df.to_excel('bluebungalow_listpage.xlsx',index=False)


    df = pd.read_excel('BlueBungalow/bluebungalow_listpage.xlsx').drop_duplicates(['pro_id'])
    for i in range(len(df)):
    # for i in range(2):
        row = df.iloc[i].to_dict()
        detailpage(row)

    df = pd.DataFrame(products)
    df.to_excel('blue14_detailpage.xlsx',index=False)
    



