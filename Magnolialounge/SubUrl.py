import requests
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'


Urls = []
def allUrl():
    url =  'https://www.magnolialounge.com.au/'
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    link_all = soup.find_all('a','navlink navlink--grandchild')
    for i in link_all:
        links = 'https://www.magnolialounge.com.au'+i.get('href')
        # print(links)
        data ={
            'links':links
        }
        print(data)
        Urls.append(data)

allUrl()
df = pd.DataFrame(Urls)
df.to_excel('Magnolia_URLS.xlsx',index=False)