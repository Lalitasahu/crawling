import re
import requests
import pandas as pd
from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html
s = Session()
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Origin': 'https://in.sugarcosmetics.com',
    'Connection': 'keep-alive',
    'Referer': 'https://in.sugarcosmetics.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

json_data = {
    'collection_handle': 'best-sellers',
    'sort': 'relevance',
    'filter': {},
    'skip': 20,
    'count': 20,
    'device_id': 'b747-98bb-4529-8c99-e5398b2f52c3',
}

def detailpage(url):
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    try:
        available_offer = soup.find('div','container-fluid px-3 mt-2 col-9 col-sm-12 col-lg-12 DesktopProduct_offerMainDiv__aXB_p').text
    except:
        available_offer = ''

    try:
        description = soup.find('div','MuiAccordionDetails-root css-l9xe8y').text
    except:
        description = ''
    
    try:
        image = re.search('"src":"(.*?)",',r.text).group(1)
    except:
        image = ""

    data = {
        'available_offer':available_offer,
        'description':description,
        
    }
    print(data)
    return data




allData = []
def listpage(url):
    response = requests.post(url)

    json_data = {
           'collection_handle': re.search('"collection_handle":"(.*?)",',response.text).group(1)
        }
    skip = 0
    nextpage = 1
    while nextpage:
            
            json_data['skip'] = skip
            response = requests.post('https://prod.api.sugarcosmetics.com/collections/prod/getCollectionv2',headers=headers, json=json_data)
            # json_data['collection_handle'] = re.search('"collection_handle":"(.*?)",',response.text).group(1)
            

            js = response.json()
            print(response.url)
            total_count = js['resbody']['total_count'][0]
            
            if skip > total_count:
                nextpage = 0
            products = js['resbody']['result']
            for product in  products:
                pro_id = product.get('id')
                title = product.get('product_json')['title']
                link = 'https://in.sugarcosmetics.com/products/'+product.get('handle')
                rating = product.get('average_rating')
                count_rating = product.get('rating_count')
                product_created_at = product.get('product_created_at')
                detail = detailpage(link)

                data = {
                    'pro_id': pro_id,
                    'title':title,
                    'link':link,
                    'rating':rating,
                    'count_rating':count_rating,
                    'product_created_at':product_created_at,
                    'category':json_data['collection_handle']
                    
                    }
                data.update(detail)
                allData.append(data)
            # print(allData)
            skip += 20 

url =['https://in.sugarcosmetics.com/makeup','https://in.sugarcosmetics.com/skin-care-products','https://in.sugarcosmetics.com/blend-trend-makeup-brush',
    'https://in.sugarcosmetics.com/collections/gifting']
for i in url:
    listpage(i)
df = pd.DataFrame(allData)
df.to_excel('sugarcosmetic_list.xlsx',index=False)