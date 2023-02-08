import requests
import re
from bs4 import BeautifulSoup as bs
from requests import Session
import pandas as pd
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

def searchkey(url):
    m_url = row['category']
    keyword = m_url
    page = 1
    nextpage = True
    while nextpage:
        m_url = f'https://shopcuup.com/search?q={keyword}&page=1'
        url = f'https://c22xk5.a.searchspring.io/api/search/search.json?lastViewed=10401&userId=c5b7242c-c800-4cd4-8bb1-5e26edeea80a&domain=https://shopcuup.com/search?q={keyword}&page={page}&siteId=c22xk5&page={page}&resultsPerPage=56&bgfilter.ss_is_content=0&q={keyword}&redirectResponse=full&resultsFormat=native'
        r = s.get(url)
        js = r.json()
        if page > js['pagination']['totalPages']:
            nextpage = False
        # print(r,url)
        products = js['results']
        print(products)
        for i in products:
            name = i.get('name')
            id = i.get('id')
            brand = i.get('brand')
            price = i.get('price')
            msrp = i.get('msrp')
            pro_url = i.get('url')
            product_type = i.get('product_type')
            images = i.get('imageUrl')

            data = {
                'landingpageUrl':m_url,
                'keyword':keyword,
                'name':name,
                'id':id,
                'brand':brand,
                'price':price,
                'msrp':msrp,
                'Pro_url':pro_url,
                'product_type':product_type,
                'images':images
            }
            print(data)
            listpagedata.append(data)
        page += 1

listpagedata = []
df = pd.read_excel('keyword.xlsx')
for i in range(len(df)):
    row = df.iloc[i].to_dict()
    searchkey(row)
    
df = pd.DataFrame(listpagedata)
df.to_excel('search_category1.xlsx',index=False)

'https://c22xk5.a.searchspring.io/api/search/search.json?lastViewed=10401%2C10101&userId=c5b7242c-c800-4cd4-8bb1-5e26edeea80a&domain=https%3A%2F%2Fshopcuup.com%2Fsearch%3Fq%3Ddemi%26page%3D1&siteId=c22xk5&resultsPerPage=56&bgfilter.ss_is_content=0&q=demi&resultsFormat=native'
'https://c22xk5.a.searchspring.io/api/search/search.json?lastViewed=10401&userId=c5b7242c-c800-4cd4-8bb1-5e26edeea80a&domain=https://shopcuup.com/search?q=demi&page=1&siteId=c22xk5&page=1&resultsPerPage=56&bgfilter.ss_is_content=0&q=demi&redirectResponse=full&resultsFormat=native'