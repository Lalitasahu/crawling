import re
import json
import requests
import pandas as pd
from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html
s = Session()
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"




def detaipage(url):
    r = s.get(url)
    print(r.url)
    soup = bs(r.text,'html.parser')
    item = dict()
    br = []
    brs =''
    for i in soup.find_all('li','arrow-r'):
        breadcrumbs = i.text
        br.append(breadcrumbs)
        brs='||'.join(br)   
    try:
        Name = soup.find('h1').text
    except:
        Name = ''
    try:
        price = soup.find('div','prod-price text-0 mt-5 mb-5 font-w-700').text
    except:
        price = ''

    try:
        like = soup.find('div','mt-10 mb-20').text.strip('\xa0')
    except:
        like = ""
    
    try:
        map = soup.find('a','gMap').get('href')
    except:
        map = ''
    
    try:
        image = soup.find('div','prod-img-box text-center relative').find('img').get('src')
    except:
        image = ''

    # for p in soup.find_all('div','extra-details mt-20'): # minispecification 
        # pr = p.text
    try:
        Product_Description = soup.find('div','co-details').find('p').text.strip()
    except:
        Product_Description =''

    try:

        pro_de={}
        pro_detail = soup.find('div','moreProdDetais d-flex flex-wrap')
        for i in pro_detail.find_all('div','moreDetail'):
                 key = i.find('span','title d-block').text
                 value = i.find('span','title d-block').text
                 pro_de[key] = value

    except:
        pro_de=''

    try:
        company_details = soup.find('p','mt-10 cpDisc').text.strip()
    except:
        company_details =''

    try:
        d ={}
        ul = soup.find("ul",'co-features-list d-flex flex-wrap mt-20')
        if ul:
         for span in ul.findAll("span",'co-feature-des d-inline-block'):
             keys = span.find("span",'title d-block').text.strip()
             values = span.find("span",'title-des d-block').text.strip()
             d[keys]=values
           
    except:
        d = ''
    # tree = html.fromstring(r.text)

    # busines_type = tree.xpath("//span[contains(string(),'BUSINESS TYPE')]//following-sibling::span//text()")
    # establishhment = tree.xpath("//span[contains(string(),'ESTABLISHMENT')]//following-sibling::span//text()")
    # certification = tree.xpath("//span[contains(string(),'CERTIFICATION')]//following-sibling::span//text()")
    data ={
        'breadcrumbs':brs,
        'name': Name,
        'price':price,
        'like':like,
        'map':map,
        'image':image,
        'Product_Description':Product_Description,
        'pro_details':pro_de,
        'company_details':company_details,
        'company_feature':d,
    }
    return data


l = []
def listpage(url):
        
  for page in range(1,2):
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    products = soup.find_all('div','bx--col-sm-4 bx--col-md-6 bx--col-lg-11 product-listing d-flex')

    for product in products:
        link = 'https://www.tradeindia.com'+product.find('a').get('href')
        detail = detaipage(link)
        data ={
            'link':link
        }
        data.update(detail)

        l.append(data)
        print (l)





url = 'https://www.tradeindia.com/manufacturers/apple-extract.html'
listpage(url)
df = pd.DataFrame(l)
df.to_excel('Tradeindia.xlsx',index=False)