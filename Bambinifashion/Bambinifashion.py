import requests 
import re
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import session
s = session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'



def crwar_detail(url):
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    page = 1
    nextpage = True
    # while nextpage:
    pages = int(soup.find('h2','category-list-title').text.replace(' Items',''))//60
    for page in range(pages+1):
        url = f'https://bambinifashion.com/happy-girls/page={page}'
        r = s.get(url)
        soup = bs(r.text,'html.parser')
        products = soup.find_all('div','category-list-product has-size-tooltip product-card')
        for product in products:
            brand = product.find('div','product-card-brand').text.strip()
            name =  product.find('div','product-card-title').text
            size = product.find('div','product-card-sizes').text
            listPrice = product.find('span','product-price-regular').text
            image = product.find('div','product-image-carousel-images').find('img').get('data-srcset')
            pro_url = 'https://bambinifashion.com'+product.find('a','product-image-carousel').get('href')
            
            data ={
                'brand':brand,
                'name':name,
                'size':size,
                'listPrice':listPrice,
                'image':image,
                'pro_url':pro_url
            }
            print(data)
            listpagedata.append(data)
        # nextpage =  


listpagedata = [ ]
url = 'https://bambinifashion.com/happy-girls/page=1'
crwar_detail(url)
df = pd.DataFrame(listpagedata)
df.to_excel('Bambinifashion.xlsx',index=False)