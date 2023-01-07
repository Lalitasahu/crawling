import requests 
import time 
import csv
from requests import Session
from bs4 import BeautifulSoup as bs
import pandas as pd
from lxml import html
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

alldata = [ ]
def detailpage(url):
    url = row['link']
    print(url)
    r = s.get(url)
    descriptions = ' ' # UnboundLocalError: local variable 'description' referenced before assignment
    Shipping_Returns = ' '
    soup = bs(r.text, 'html.parser')
    try:
        for i in soup.find('div','product-tabs-content-inner clearfix').find_all('li'):
            descriptions = i.text
    except:
            descriptions = ''

    try:
        Shipping_Returns = soup.find('div','panel panel-default panel-custom-tab').find('div','product-tabs-content-inner clearfix').text.strip()
    except:
        Shipping_Returns = ''
    print(Shipping_Returns)

    data = {
            'descriptions':descriptions,
            'Shipping_Returns':Shipping_Returns,
    }
    alldata.append(data)
    print(data)

df = pd.read_excel('bluebungalow.xlsx')
for i in range(len(df)):
# for i in range(2):
    row = df.iloc[i].to_dict()
    detailpage(row)


df = pd.DataFrame(alldata)
df.to_excel('bluebungalow_detail.xlsx',index=False)
