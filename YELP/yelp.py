import re
import json
import requests
import pandas as pd
from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html
s = Session()
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
# with open('file.json','w') as file:
    # file.write(json.dumps(data,indent=4))
url = 'https://www.yelp.com/search?cflt=burgers&find_loc=San+Francisco%2C+CA&start={}'


def detailpage(url):
    r = s.get(url)
    # print(r.url)
    soup = bs(r.text,'html.parser')
    try:
        Title = soup.find('h1').text
    except:
        Title ='na'
    try:
        review = soup.find('a','css-1m051bw').text
    except:
        review = "na"
    try:
        address = soup.find('p','css-qyp8bo').text
    except:
        address = "na"
        
    l = soup.findAll('a','css-1um3nx')
    websiteUrl = ""
    direction = ""
    for i in l:
        if i.get("rel"):
            websiteUrl = "https://www.yelp.com{}".format(i.get("href"))
        elif  i.get("href").startswith("/map"):
            direction = "https://www.yelp.com{}".format(i.get("href"))
    data= {
        'Title': Title,
        'review': review,
        'address': address,
        'websiteUrl': websiteUrl,
        'direction': direction
    }

    return data

alldata = []
def listpage(url):
    
    for i in range(0,240,10):
        urls = url.format(i)
        r = s.get(urls)
        soup = bs(r.text, 'html.parser')
        # print(r.url)
        all_link= soup.find_all('a','css-1m051bw')
        # print(links)
        for l in all_link:
            if l.get("href").startswith("/biz"):
                pro_link = 'https://www.yelp.com'+l.get('href')
                print(pro_link)
                detail = detailpage(pro_link)
                data = {'LandingPagge':r.url,'pro_link':pro_link, 'page_rank':i}
                data.update(detail)
                alldata.append(data)
        # print(js)
        # if soup.find('a','next-link navigation-button__09f24__m9qRz css-144i0wq'):
        #     nextpage = soup.find('a','next-link navigation-button__09f24__m9qRz css-144i0wq').get('href')
        #     print(f'THIS IS NEXT PAGE.. {nextpage}................................')
        # else:
        #     nextpage = False


listpage(url)
# detailpage(url)
df = pd.DataFrame(alldata)
df.to_excel('yelp.xlsx',index=False)
print(alldata)