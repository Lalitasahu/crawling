import requests
from bs4 import BeautifulSoup as bs
from requests import Session 
import pandas as pd
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

q = 'pajama'
def searchkeys(url):
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    total_count = soup.find('span','prdCount').text.split(' ')[0].replace('(','')
    nextpage = True
    page = 1
    while nextpage:
        if page < int(total_count):
            api = f'https://www.clovia.com/search/ajax/?page={page}&style=&apply_filter=&q=pajama'
            r = s.get(api)
            # print(r,r.url)
            soup = bs(r.text, 'html.parser')
            products = soup.find_all('li',{'total_count':'2459'})
            for product in products:

                try:
                    name = product.find('a','catName').text.strip()
                except:
                    name = ''
            
                try:
                    pro_link = product.find('a','catName').get('href')
                except:
                    pro_link = ''

                try:
                    first_price = product.find('span','pull-left listingPrice').text.split('\n')[0]
                except:
                    first_price = ''
                
                try:
                    second_price = product.find('span','pull-left listingPrice').find('del').text
                except:
                    second_price = ''
                
                try:
                    image = [im.get('src') for im in product.find('div','pdImg').find_all('img')]
                except:
                    image = ''
                data = {
                    'name':name,
                    'pro_link':pro_link,
                    'first_price':first_price,
                    'second_price':second_price,
                    'image':image
                }
                print(data)
                searching.append(data)
        else:
            nextpage = False
        page += 1
searching = []
url = 'https://www.clovia.com/search/?q=pajama'
searchkeys(url)
df = pd.DataFrame(searching)
df.to_excel('searchingkeys_night.xlsx',index=False)


