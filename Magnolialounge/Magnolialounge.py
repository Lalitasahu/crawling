import requests
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'



def detailpage(url):
    r = s.get(url)
    soup = bs(r.text,'html.parser')

    try:
        description = soup.find('div','product__description__content__entry').text.strip()
    except:
        description = ''
    
    try:
        review = soup.find('span','jdgm-prev-badge__text').text.strip()
    except:
        review = ''

    try:
        values = [i.text for i in soup.find_all('div','accordion__body')]
    except:
        values = ''
    
    try:
        keys = [i.text for i in soup.find_all('h4','accordion__title')]
    except: 
        keys = ''
    info = dict(zip(keys,values))
    Sizing = info['Sizing']
    Shipping = info['Shipping']
    Returns = info['Returns']

    data = {
        'description':description,
        'Sizing':Sizing,
        'Shipping':Shipping,
        'Returns':Returns,
        'review':review

    }
    # print(data)
    return data

alldata = []
def listpage(url):
    # url = 'https://www.magnolialounge.com.au/collections/young-spirit?page={}'
    url = row['link']
    next = url
    print(next)
    while next:
        r = s.get(next)
        # print(r.url)
        soup = bs(r.text,'html.parser')
        products = soup.find_all('div','product-item')
        for product in products:
            name = product.find('span','product__grid__title__default').text
            link = 'https://www.magnolialounge.com.au'+product.find('a','product-link product-link--info').get('href')
            price  = product.find('span','new-price').text.strip()
            # for i in soup.find_all('div','product-item__bg'):
                # image = i.get('data-bgset').split(',')[0]
            image = ','.join(['https:'+i.get('data-bgset').split(',')[0] for i in product.find_all('div','product-item__bg')])
            details = detailpage(link)

            deta = {
                'landingUrls': row['link'],
                'name': name,
                'link' : link,
                'price' : price,
                'image' : image,
                
            }
            deta.update(details)
            alldata.append(deta)
            print(deta)
        try:
            nextpage = soup.find('ul','pagination-custom').find_all('a')

            # print(nextpage)
            for i in nextpage:
                if i.get('title') == 'Next »':
                    # print(i)
                    next = 'https://www.magnolialounge.com.au'+i.get('href')
                    print(f'..............................{next}..................................')
                    break
                else:
                    next = False
        except:
            next = False
            
df = pd.read_excel('Magnolia_URLS.xlsx')
for i in range(len(df)):
# for i in range(1,3):
    row = df.iloc[i].to_dict()
    listpage(row)

# url = 'https://www.magnolialounge.com.au/collections/womens-loungewear?page=1'
# url = 'https://www.magnolialounge.com.au/collections/young-spirit?page=1'
# listpage(url)
df = pd.DataFrame(alldata)
df.to_excel('Magnolialounge.xlsx', index=False)   