import requests
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
# url = 'https://www.magnolialounge.com.au/collections/best-selling-au/products/icy-rose-canvas-mini-backpack?variant=41897397780722'

allreviews = []
def review(url):
    url = row['link']
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    allreview = soup.find_all('div','jdgm-rev jdgm-divider-top')
    for i in allreview:
        try:
            name = i.find('span','jdgm-rev__author').text
        except:
            name = ''
        
        try:
            sub_title = i.find('b','jdgm-rev__title').text
        except:
            sub_title = ''
        
        try:
            comment = i.find('div','jdgm-rev__body').text
        except:
            comment = ''

        try:
            star = i.find('span','jdgm-rev__rating').get('data-score')
        except:
            star = ''


        data = {
            'name':name,
            'sub_title':sub_title,
            'comment':comment,
            'star':star

        }
        print(data)
        allreviews.append(data)

df = pd.read_excel('Magnolialounge.xlsx')
for i in range(len(df)):
    row = df.iloc[i].to_dict()
    review(row)



df = pd.DataFrame(allreviews)
df.to_excel('magnolia_reviews.xlsx',index=False)