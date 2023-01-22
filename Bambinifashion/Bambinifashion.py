import requests 
import re
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import session
s = session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'



def crwar_detail():
    url = 'https://bambinifashion.com/lifestyle'
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    products = soup.find_all('div','category-list-product has-size-tooltip product-card')
    for product in products:
        brand = product.find('div','product-card-brand').text.strip()
        name =  product.find('div','product-card-title').text
        size = product.find('div','product-card-sizes').text
        listPrice = product.find('span','product-price-regular').text
        image = product.find('div','product-image-carousel-images').find('img').get('data-srcset')
        pro_url = product.find('a','product-image-carousel').get('href')
        
    print(r)

crwar_detail()