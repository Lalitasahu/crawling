import requests 
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

def review(url):
    cat =  url.split('/')[-2]
    page = 1 
    nextpage = True
    while nextpage:
        api = f'https://www.clovia.com/web/api/v1/product/{cat}/web-reviews/s/?page={page}'
        r = s.get(api)
        js = r.json()
        # print(js.keys())
        if js['number'] < js['num_pages']:
            print(r,r.url)
            review = js['object_list']
            for i in review:
                name = i[6]
                id = i[0]
                comment = i[2] 
                date = i[7]
                star = i[9]

                data = {
                    'landinpage':url,
                    'name':name,
                    'id':id,
                    'comment':comment,
                    'date':date,
                    'star':star
                }
                
                print(data)
                allreview.append(data)
        else:
            nextpage = False
            # break
        page += 1


allreview = []
url = 'https://www.clovia.com/product/skivia-onion-oil-mini-conditioner-with-sunflower-coconut-oil-30-ml/'
review(url)
df = pd.DataFrame(allreview)
df.to_excel('reviews.xlsx',index=False)