import requests 
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
# url = 'https://www.maccosmetics.in/product/13825/102515/products/skincare/primer/studio-radiance-moisturizing-illuminating-silky-primer?size=30_ml'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.maccosmetics.in/',
    'Origin': 'https://www.maccosmetics.in',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}

params = {
    'paging.from': '0',
    'paging.size': '10',
    'filters': '',
    'search': '',
    'sort': 'Newest',
    'image_only': 'false',
    'page_locale': 'en_IN',
    '_noconfig': 'true',
    'apikey': '1d01c6a1-3fb0-429d-9b01-7b3d915933af',
}

allreviews = []
def reviews(url):
    url = row['Product_URL']
    # r = s.get(url)
    print(url)
    id = url.split('/products/')[0]
    pro_id = id.split('/')[-1]
    print(pro_id)
    nextPage = True
    num = 0
    while nextPage:
        params['paging.from'] = str(num)
        response = requests.get(f'https://display.powerreviews.com/m/269258/l/all/product/{pro_id}/reviews',
        params=params,
        headers=headers,
        )
        # print(response.url)
        # print(params)


        js = response.json()
        # print(js)
        # current_page_number = js['results']
        # print(current_page_number)
        # print(js['paging']['current_page_number'] ,js['paging']['pages_total'])
        if js['paging']['current_page_number'] <= js['paging']['pages_total']:
            num += 10
            nextPage = True
        else:
            nextPage = False


        products = js['results'][0]['reviews']
        for review in products:
            Name = review.get('details').get('nickname')
            Headline = review.get('details').get('headline')
            Shade_Name = review.get('details').get('product_name')
            Comments = review.get('details').get('comments')
            merchant_response = review.get('details').get('merchant_response')
            location = review.get('details').get('location')
            created_date = review.get('details').get('created_date')
            Product_page_id = review.get('details').get('product_page_id')
            product_variant = review.get('details').get('product_variant')
        

            data = {
                'Name':Name,
                'Headline':Headline,
                'Shade_Name':Shade_Name,
                'Comments':Comments,
                'merchant_response':merchant_response,
                'location':location,
                'created_date':created_date,
                'Product_page_id':Product_page_id,
                'product_variant':product_variant,        
            }
            print(data)
            allreviews.append(data)          


df = pd.read_excel('Macecostmetic1.xlsx')
for i in range(len(df)):
# for i in range(2):
    row = df.iloc[i].to_dict()
    reviews(row)

# url = 'https://www.maccosmetics.in/product/13825/102515/products/skincare/primer/studio-radiance-moisturizing-illuminating-silky-primer?size=30_ml'


df = pd.DataFrame(allreviews)
df.to_excel('mac__rev.xlsx',index=False)