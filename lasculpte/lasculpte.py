import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import Session
s=Session()
s.headers['user-agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"

def crwal_detail(url):
    r=s.get(url)
    soup=bs(r.text,'html.parser')
    description=soup.find('div','accordion-inner').text.strip()
    images=imgs=soup.find('div','col').find_all('img')
    image = []
    for i in images:
        img=i.get('data-src')
        if img:
            image.append(img)

    data={'description': description,
        
        'images':"|".join(image) 
        
        }
    return data


all_data=[]
def crwal_list():
    url='https://www.lasculpte.com.au/collections/shapewear/'
    next_page=url
    while next_page:
        r=s.get(url)
        print(url)
        soup=bs(r.text,'html.parser')
        products=soup.find_all('div','image-fade_in_back')
        for i in products:
            link=i.find('a').get('href')
            detail=crwal_detail(link)
            d={'link':link}
            d.update(detail)
            all_data.append(d)
    if soup.find('a','page-number').get('href'):
        next_page=soup.find('a','page-number').get('href')
        print(f'NEXT PAGE.. {next_page}.................................')
    else:
        next_page=False

crwal_list()
df=pd.DataFrame(all_data)
df.to_excel('lasculpte.xlsx',index=False)
print(all_data)
