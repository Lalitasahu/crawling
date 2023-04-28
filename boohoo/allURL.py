import requests
import json
import time
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import Session 
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
alldata = []
url = 'https://www.boohoo.com'
r = s.get(url)
soup = bs(r.text,'html.parser')
for i in soup.find_all('div','b-menu_item-submenu b-menu_subpanel-content m-level_3_content'):
    link = i.find_all('a','b-menu_item-link m-regular')
    for j in link:
        allurl = j.get('href')
        Name = j.text.strip()
        data = { 'allurl':allurl, 'Name':Name }
        print(allurl)   
        alldata.append(data)

df = pd.DataFrame(alldata)
df.to_excel('allurls.xlsx',index=False)