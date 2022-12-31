import requests
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"


def detailpage(url):
    r = s.get(url)
    soup = bs(r.text,'html.parser')

    try:
        breadcrumbs = soup.find('ul','breadcrumbs font--paragraph').text
    except:
        breadcrumbs = ''

    try:
        selling_price = soup.find('span','actual-price').text
    except:
        selling_price = ''
    
    try:
        list_price = soup.find('span','money font--light-accent').text
    except:
        list_price = ' '
    
    try:
        Description = soup.find('div','rte-content').text.replace('\n\xa0','').replace('\n','')
    except:
        Description = ''

    try:
        images='||'.join([image.get('data-src') for image in soup.find('div','product-page--thumbs-container').find_all('img')])
        # image = soup.find('div','product-page--thumbs-container').find_all('img')
        # img = []
        # for i in image:
            # img = i.get('data-src')#.replace('{width}','600')
            # img.append(im)
    except:
        images = ''
    
    # print(img)
    data ={
        'breadcrumbs':breadcrumbs,
        'selling_price':selling_price,
        'list_price':list_price,
        'Description':Description,
        'images':images
    }
    return data
alldata = []
def listpage(url):
    
    nextpage = url
    # for i in range(1,5):
    while nextpage:
        # urls = url.format(i)
        # print(nextpage)
        r = s.get(nextpage)
        soup = bs(r.text,'html.parser')
        products = soup.find_all('div','product--root')
        
        for product in products:
            try:
                pro_url = 'https://bebellacosmetics.com'+product.find('div','product--details').find('a').get('href')
            except:
                pro_url = ''

            try:
                Name = product.find('div',"product--title font--block-heading").text
            except:
                Name = ''
            
            try:
                price = product.find('span','money').text
            except:
                price = ''

            try:
                image = 'https:'+product.find('img','lazypreload').get('data-src').replace('{width}','600')
            except:
                image = ''

            detail = detailpage(pro_url)
            data = {
                'pro_url':pro_url,
                'Name':Name,
                'price':price,
                'List_image':image
            }
            data.update(detail)
            print(data)
            alldata.append(data)
        try:
            nextpage = 'https://bebellacosmetics.com'+soup.find('li','arrow right').find('a').get('href')
            print(f'...............{nextpage}...............................')
        except:
            nextpage = False

       

url = 'https://bebellacosmetics.com/collections/new-arrivals?page=1'
listpage(url)
df = pd.DataFrame(alldata)
df.to_excel('BeBella.xlsx',index=False)



# https://www.myglamm.com/buy/makeup/lips/lipstick