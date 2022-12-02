import pandas as pd
import re
import requests
from bs4 import BeautifulSoup as bs
from requests import Session

s=Session()
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
url='https://www.myntra.com/hair-dryer'
r=s.get(url)
ll=[]
pro_Link=[]
name= re.findall('"product":"(.*?)",',r.text)
links=re.findall('"landingPageUrl":"(.*?)",',r.text.replace('u002F','').replace('\\','/'))
for i in links:
    link='https://www.myntra.com/'+i
    pro_Link.append(link)
price=re.findall('"price":(.*?),',r.text)
mrp=re.findall('"mrp":(.*?),',r.text)
off=re.findall('"discountDisplayLabel":(.*?),',r.text)


for n,l,p,m,o, in zip(name,pro_Link,price,mrp,off):
    d={'name':n,'link':l,'price':p,'mrp':m,'off':o}
    ll.append(d)


df=pd.DataFrame(ll)
df.to_excel('myn.xlsx',index=False)
print(ll)