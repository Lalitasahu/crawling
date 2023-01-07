import requests 
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

alldata = []
def allproduct():
    url = 'https://bluebungalow.com.au/collections/dresses'
    r = s.get (url)
    soup = bs(r.text,'html.parser')
    for i in soup.find('ul','top-navigation').find_all('a','title-level1'):
        Suburl = i.get('href') 



    # for i in soup.find('div','navigation-wrapper').find_all('li','level0 level-top parent'): 
    #     link = i.find('a','level-top').get('href')  # only main urls of site 

      
    # for i in soup.find_all('li','level1 groups item'):
    #     Suburl = i.find('a').get('href')

    # for i in soup.find_all('div','level0 menu-wrap-sub'):
    #     for j in i.find('ul').find_all('li'):
    #         uld = j.find('a').get('href')
    #         if 'https://' in uld:
    #             url = uld
    #         else:
    #             url = 'https://bluebungalow.com.au'+uld

    #         name = j.find('a').text.strip()
        data ={
            'SubUrl':Suburl,
            # 'name':name
        }
        alldata.append(data)
        print(data)
allproduct()
df = pd.DataFrame(alldata)
df.to_excel('bluebungalow_cat_Url.xlsx',index=False)