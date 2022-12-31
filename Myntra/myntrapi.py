import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from requests import Session
import re
s=Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'


def detailpage(url):
    r=s.get(url)
    
    
    # print(id)
    # return {'id':id,'brand':brand,'price':price,'image':image}
    # return data

    

l=[]
def listPage():
    url='https://www.myntra.com/hand-cream'
    r=s.get(url)
    ll=[]
    links=re.findall('"landingPageUrl":"(.*?)"',r.text.replace('u002F','').replace('\\','/'))
    name= re.findall('"product":"(.*?)",',r.text)
    for i,nm in zip(links,name):
        link='https://www.myntra.com/'+i
        # for j in link:
        # ll.append(link)
        detail=detailpage(link)
        d={'links':link,
            'name':nm,
            'id':detail['id'],
            'brand':detail['brand'],
            'price':detail['price'],
            'image':detail['image']}
        print(d)
        
        # d.update(detail)
        l.append(d)

listPage()
df=pd.DataFrame(l)
df.to_excel('mytapi.xlsx',index=False)

# url='https://www.myntra.com/gateway/v2/product/16099550/cross-sell'
# detailpage(url)
print(l)