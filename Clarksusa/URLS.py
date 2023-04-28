import requests 
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import session
s = session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
# url = 'https://www.clarksusa.com/womens/all-styles/c/w2'

listall = [ ]
def allUrl():
    url = 'https://www.clarksusa.com'
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    urls = soup.find('ul','new-header__flyout-menu-column-list').find_all('li')
    for i in urls:
        link = 'https://www.clarksusa.com'+i.find('a','new-header__flyout-menu-column-list-item-link').get('href')
        print(link)
        data = {
            'link':link
        }
        listall.append(data)

allUrl()
df = pd.DataFrame(listall)
df.to_excel('SusaUrls.xlsx',index=False)