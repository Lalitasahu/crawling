import requests
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import Session

s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'


alldata = []
def listpage(url):
    # url = 'https://www.magnolialounge.com.au/collections/young-spirit?page={}'
    nextpage = url
    while nextpage:
    # for i in range(1,6):
        # urls = url.format(i)
        r = s.get(url)
        soup = bs(r.text,'html.parser')
        products = soup.find_all('div','product-item')
        for product in products:
            name = product.find('span','product__grid__title__default').text
            # print(name)
            deta = {
                'name': name
            }
            alldata.append(deta)
        next = soup.find_all('li','pagination-custom__arr')
        for i in next:
            nextpage= 'https://www.magnolialounge.com.au'+i.find('a',{"title":"Next »"})

        if next:
            nextpage = nextpage
            print(f'..............................{nextpage}..................................')
        else:
            nextpage = False

url = 'https://www.magnolialounge.com.au/collections/young-spirit?page=1'
listpage(url)
df = pd.DataFrame(alldata)
df.to_excel('Magnolialounge.xlsx', index=False)   