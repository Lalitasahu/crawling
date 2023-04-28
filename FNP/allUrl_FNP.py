import requests 
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
url = 'https://www.fnp.com'
r = s.get(url)
soup = bs(r.text,'html.parser')
alllink =  []
l = [i.find_all('li') for i in soup.find_all('div','sub-navmenubar')]
for i in l:
     for j in  i:
        link = 'https://www.fnp.com'+j.find('a').get('href')
        name = j.find('a').text
        data = {
            'name':name,
            'link':link
        }
        print(data)
        alllink.append(data)

df = pd.DataFrame(alllink)
df.to_excel('Urls_FNP.xlsx',index=False)