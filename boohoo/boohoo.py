import requests
import json
import time
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import Session 
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
# url = 'https://www.boohoo.com/mens/new-in'

def crwal_detailpage(url):
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    D_name = soup.find('h1').text.strip()
    D_price = soup.find('div','b-product_details-price').find('span','b-price-item').text.strip()
    color = soup.find('span','b-variation_label-value').text.strip()
    size = soup.find('span','b-variation_swatch-value_text').text
    bread = [i.text.strip() for i in soup.find('nav','b-breadcrumbs').find_all('span')]
    product_Detail = soup.find('div','b-product_details-content').text.strip()
    Return = soup.find('div','b-product_shipping-returns_content').text.strip()
    image1 = soup.find('div',id='product_gallery_track').find('img').get('src')
    image2 = soup.find('div',id='product_gallery_track').find('img').get('src')+'_1'
    data ={
        'D_name':D_name,
        'D_price':D_price,
        'color':color,
        'size':size,
        'bread':bread,
        'product_Detail':product_Detail,
        'Return':Return,
        'image1':image1,
        'image2':image2
    }
    return data

alldata = []
def crwal_listpage():
    start = 40
    nextpage = True
    while nextpage:
        api = f'https://www.boohoo.com/womens/dresses?start={start}&sz=40'
        # api = f'https://www.boohoo.com/mens/new-in?start={start}&sz=40'
        time.sleep(4)
        # api = f'https://www.boohoo.com/on/demandware.store/Sites-boohoo-UK-Site/en_GB/Search-UpdateGrid?cgid=mens-newin&start={start}&sz=40&selectedUrl=https://www.boohoo.com/on/demandware.store/Sites-boohoo-UK-Site/en_GB/Search-UpdateGrid?cgid=mens-newin&start={start}&sz=40&ajax=true'
        r = s.get(api)
        print(r.url)
        soup = bs(r.text,'html.parser')
        products = soup.find_all('section','b-product_tile')
        if products:
            for product in range(len(products)):
                Name = products[product].find('h3').find('a').text.strip()
                pro_link = 'https://www.boohoo.com'+products[product].find('h3').find('a').get('href')
                info = json.loads(products[product].find('h3').find('a').get('data-analytics'))
                id = info['id']
                category1 = info['category1']
                price = '£'+info['price']
                itemId = info['itemId']
                details = crwal_detailpage(pro_link)
                data = {
                    'landingURL':r.url,
                    'product_rank':product,
                    'Name':Name,
                    'pro_link':pro_link,
                    'id':id,
                    'category1':category1,
                    'price':price,
                    'itemId':itemId,
                }
                data.update(details)
                print(data)
                alldata.append(data)
        else:
            break
        start += 40
        
crwal_listpage()
df = pd.DataFrame(alldata)
df.to_excel('boohooAll.xlsx',index=False)

