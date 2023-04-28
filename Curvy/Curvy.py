import requests
import pandas as pd
from requests import Session
from bs4 import BeautifulSoup as bs
s=Session()
s.headers['user-agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"


def crwal_detail(url):
    r=s.get(url)
    soup=bs(r.text,'html.parser')
    name=soup.find('h1','product-single__title').text
    description=soup.find('div','rte').text
    imgs=soup.find_all('div','product__thumb-item')
    for im in imgs:
        img_link='https://www.curvyswimwear.com.au'+im.find('img').get('data-src')
        
    data={
        'name':name,
        'description':description,
        'img_link':img_link
    }
    print(data)
    return data

l=[]

def crawl_list_while(row):
    # while next_page:
    urls='https://www.curvyswimwear.com.au/collections/womens-swimwear-australia?filter.v.availability=1&page=1'
    # total=int (278/48)
    # for u in range(0,total):
    next_page = urls
    while next_page:
        url=urls.format(urls)
        r=s.get(url)
        print(r.url)
        soup=bs(r.text,'html.parser')
        p_link=soup.find_all('a','grid-item__link')
        for product in p_link:
            link='https://www.curvyswimwear.com.au'+product.get('href')
            detail=crwal_detail(link)
            d={'link':link,
                'name': detail['name'],
                'description': detail['description'],
                'img_link': detail['img_link'],
                "sub_category":row['Folded Name'],
                "category":row['Gender Folder'],
                "cat_url":row['url']   
            }
            print(d)
            l.append(d)
        if soup.find('a','btn btn--large btn--circle btn--icon').get('href'):
            next_page=soup.find('a','btn btn--large btn--circle btn--icon').get('href')
            print(f'NEXT PAGE.. {next_page}.................................')
        else:
            next_page = False



def crawl_list(row):
    # while next_page:
    urls='https://www.curvyswimwear.com.au/collections/womens-swimwear-australia?filter.v.availability=1&page={}'
    total=int (278/48)
    for u in range(0,total):
        url=urls.format(u)
        r=s.get(url)
        print(r.url)
        soup=bs(r.text,'html.parser')
        p_link=soup.find_all('a','grid-item__link')
        for product in p_link:
            link='https://www.curvyswimwear.com.au'+product.get('href')
            detail=crwal_detail(link)
            d={'link':link,
                'name': detail['name'],
                'description': detail['description'],
                'img_link': detail['img_link'],
                "sub_category":row['Folded Name'],
                "category":row['Gender Folder'],
                "cat_url":row['url']   
            }
            print(d)
            l.append(d)
        # if soup.find('a','btn btn--large btn--circle btn--icon').get('href'):
        #     next_page=soup.find('a','btn btn--large btn--circle btn--icon').get('href')
        #     print(f'NEXT PAGE.. {next_page}.................................')
        # else:
        #     next_page = False

df = pd.read_excel('input.xlsx')
for i in range(len(df)):
    row = df.iloc[i].to_dict()
    crawl_list_while(row)


df=pd.DataFrame(l)
df.to_excel('Curvy.xlsx',index=False)
# crwal_list()