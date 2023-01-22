import requests 
import re
import math
from requests import Session
from bs4 import BeautifulSoup as bs
import pandas as pd
from lxml import html
import concurrent.futures
import time
import random

s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

params = {
    'productId': '6830889336966',
    'productName': 'Calla Aqua Palm Crinkle Dress',
    'productSKU': 'ONE-DW2F-Pnt15-8',
    'page': '2',
    'apiKey': 'pubkey-7Gc72P63He8d1Gz7MNT197220938iJ',
    'storeUrl': 'bluebungalow.myshopify.com',
    'take': '5',
    'sort': 'recent',
}
allreviews = []
def review(url):
    url = row['link']
    time.sleep(random.randrange(1,4))
    r = s.get(url)
    print(url)
    soup = bs(r.text,'html.parser')
    try:
        product_id = re.search('ProductID: (.*?),',r.text).group(1)
    except:
        product_id = ''
    
    try:
        product_name = soup.find('div','breadcrumbs-inner').find_all('span')[1].text.strip()
    except:
        product_name = ''

    try:
        productSKU = re.search('"sku":"(.*?)",',r.text).group(1)
    except:
        productSKU = ''
    page = 1
    
    while True:
        params['productId'] = product_id
        params['productTitle'] = product_name
        params['productSKU'] = productSKU
        params['page'] = str(page)
        response = requests.get('https://stamped.io/api/widget', params=params)
        js = response.json()
        totalreview = js['count']
        soup = bs(js['widget'],'html.parser')
        allreview = soup.find_all('div','stamped-review')
        # print(allreview)
        for i in allreview:
            name = i.find('div','stamped-review-header').find('strong').text    
            # Verified_Buyer = i.find('div','stamped-review-header').find('span').text
            subtitle = i.find('h3').text
            comment = i.find('p','stamped-review-content-body').text
            date = i.find('div','created').text
            like = i.find('div','stamped-rating-holder').find('a','stamped-thumbs-up').text.strip()
            dislike = i.find('div','stamped-rating-holder').find('a','stamped-thumbs-down').text.strip()
            # print(date)
            datas = {
                
                'landingUrl':row['link'],
                'name':name,
                'subtitle':subtitle,
                'comment':comment,
                'data':date,
                'like':like,
                'dislike':dislike,
            }
            print(datas)
            allreviews.append(datas)
        if math.ceil(totalreview/5) <= page:
            break
        page+=1

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

    df = pd.read_excel('blue14_detailpage.xlsx')
    # df = pd.read_excel('bluebungalow/blue14_detailpage.xlsx')
    for i in range(len(df)):
    # for i in range(2):
        row = df.iloc[i].to_dict()
        review(row)
        # executor.submit(review,row)


df = pd.DataFrame(allreviews)
df.to_excel('blue14_review.xlsx',index=False)
