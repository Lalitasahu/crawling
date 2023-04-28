import requests 
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import session
s = session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

allinfo = []
def detailpage(url):
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    sizeapi = 'https://www.clarksusa.com/p/26167535/getProductSizeMatrix'
    rr = s.get(sizeapi)
    js = rr.json()

    skeys = [i.get('data-code-value') for i in soup.find_all('input',attrs={'name':'size-selected'})]
    svalue = [i.get('data-prompt-value') for i in soup.find_all('input',attrs={'name':'size-selected'})]
    size = dict(zip(skeys,svalue))
    
    available = []
    stock_info = {}
    for i in size:
        stock = js[i]['FIT_4W']['availableStockAmount']
        
        if stock > 0 :
            stock_info[size[i]] = 'in stock'
        else:
            stock_info[size[i]] = 'out of stock'
        


    sale_price2 = soup.find('span','product-price-panel__price product-price-panel--reduced-price js-current-price').get('content')
    if soup.find('span','product-price-panel__price product-price-panel--reduced-price js-current-price').get('content'):
        saleprice = float(sale_price2)*0.7
    else:
        saleprice = soup.find('span','product-price-panel__price product-price-panel--previous-price js-prev-price').text.strip()

    mrp = soup.find('span','product-price-panel__price product-price-panel--previous-price js-prev-price').text.strip()
    listprice = soup.find('span','product-price-panel__price product-price-panel--reduced-price js-current-price').get('content')           
    badge = soup.find('div','product-badge__general').find('img').get('src')
    description = soup.find('div','product-description__text product-description__text--restricted').text
    product_details = {}
    for i in soup.find_all('div','product-page-tabs__specifications__description-list__row'):
        key = i.find('dt').text
        value = i.find('dd').text
        product_details = {key:value}
    bultheading = [bult.text for bult in soup.find_all('span','product-page-tabs__benefits-text--business-title')]
    bulttext = [ bult.text for bult in  soup.find_all('span','product-page-tabs__benefits-text--business-copy')]
    points = dict(zip(bultheading,bulttext))
    Comfortable =  points['Comfortable ']
    Responsible_Leather = points['Responsible \n Leather']
    images = '||'.join([i.find('img').get('src') for i in soup.find_all('picture')])
    
    data = {
        'mrp':mrp,
        'listprice':listprice,
        'saleprice':saleprice,
        'badge':badge,
        'description':description,
        'Comfortable':Comfortable,
        'Responsible_Leather':Responsible_Leather,
        'images':images,
        'stock_info':stock_info,
        'product_details':product_details

    }
    
    data.update(product_details)
    allinfo.append(data)
    print(data)
url = 'https://www.clarksusa.com/c/Clarkwell-Demi/p/26167535'
detailpage(url)
df = pd.DataFrame(allinfo)
df.to_excel('clarksusadetail.xlsx',index=False)
