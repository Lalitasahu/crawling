import requests 
import re
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import session
s = session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'


def detailpage(url):
    # url = 'https://bambinifashion.com/order66/eagle-print-long-sleeved-t-shirt-in-pink-188035.html'
    url = row['pro_url']
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    try:
        title = soup.find('h1').text.strip()
    except:
        title = ''
    
    try:
        list_price = soup.find('div','product-price').find_all('span')[0]
    except:
        list_price = ''

    try:
        sele_price = soup.find('div','product-price').find_all('span')[1]
    except:
        sele_price = ''

    try:
        off = soup.find('div','product-single-discount').find('span').text
    except:
        off = ''
    
    try:
        head = [i.text.strip() for i in soup.find_all('h3','product-tab-section-title')]
        text = [j.text.strip().replace('\t','') for j in soup.find_all('div','product-tab-section-content')]
        specification  = dict(zip(head,text))
    except:
        specification = ''
    
    try:
        images = [i.get('src') for i in soup.find('div','product-thumbnails').find_all('img')]
    except:
        images = ''

        
    data = {
        'title':title,
        'list_price':list_price,
        'sele_price':sele_price,
        'off':off,
        'specification':specification,
        'images':images
    }
    print(data)
    listpagedata.append(data)


def crwar_list(url):
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

detailpagedata = []
listpagedata = [ ]


df = pd.read_excel('Bambinifashion.xlsx')#.drop_duplicates(['pro_url'])
for i in range(len(df)):
# for i in range(2):
    row = df.iloc[i].to_dict()
    detailpage(row)
    
df = pd.DataFrame(listpagedata)
df.to_excel('detailpagedata.xlsx', index=False)

# url = 'https://bambinifashion.com/boy/sneakers-1'
# crwar_list(url)
# df = pd.DataFrame(listpagedata)
# df.to_excel('Bambinifashion.xlsx',index=False)