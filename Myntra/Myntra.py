import requests
import re
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import Session
import json
s=Session()
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"


allreview=[]
def reviews(url):
    r=s.get(url)
    print(url)

    try:
        id=re.search('"id":(.*?),',r.text).group(1)
    except:
        id='NA'
    
    try:
        Name=re.search('"userName":"(.*?)",',r.text).group(1)
    except:
        Name='NA'
    try:
        review=re.search('"review":"(.*?)"',r.text).group(1)
    except:
        review="no review"

    try:  
        rating=re.search('"userRating":(.*?),',r.text).group(1)
    except:
        rating='NA'
    
    try:
        upvotes=re.search('"upvotes":"(.*?)"',r.text).group(1)
    except:
        upvotes="NA"

    try:
        downvotes=re.search('"upvotes":"(.*?)"',r.text).group(1)
    except:
        downvotes='NA'

    rews={'id':id,
         'Name':Name,
         'review':review,
         'rating':rating,
         'upvotes':upvotes,
         'downvotes':downvotes,
      
          }
    allreview.append(rews)
    # print(rews)
    print(rews)
    return allreview


def crawl_detail(url):
    r=s.get(url)
    # print(url)

    
    try:
        brand=re.search('"brand":"(.*?)"',r.text).group(1)
    except:
        brand='NA'

    try:
        name=re.search('"name":"(.*?)"',r.text).group(1)
    except:
        name='NA'

    try:
        images='||'.join(re.findall('{"src":"(.*?)",',r.text.replace('u002F','').replace('\\','/').replace('($height)','720').replace('($qualityPercentage)','90').replace('($width)','540')))
    except:
        images='NA'

    try:
        Specifications=re.search('"Fabric":"(.*?)"},',r.text).group(1)    
    except:
        Specifications='not specification'


    try:
        CompleteTheLook=re.search('"value":"(.*?)",',r.text).group(1) # not understood 
    except:
        CompleteTheLook='no look'
    
    try:
        rating=re.search('"rating":(.*?),',r.text).group(1)
    except:
        rating='NA'
    
    try:
        totalCountraiting=re.search('"totalCount":(.*?),',r.text).group(1)
    except:
        totalCountraiting='NA'

    try:
        userName='||'.join(re.findall('"userName":(.*?),',r.text))
    except:
        userName='NA'

    try:
        reviewUser='||'.join(re.findall('"reviewText":(.*?).",',r.text))
    except:
        reviewUser='NA'

    try:
        specifications = json.loads(re.search('articleAttributes":(.*?),"systemAttr',r.text).group(1))
        sp = {}
        for i in specifications:
            if specifications[i] != 'NA':
                sp[i] = specifications[i]   
    except :
        sp = {}

    try:
        id='https://www.myntra.com/reviews/'+re.search('"id":(.*?),',r.text).group(1)
    except:
        id='NA'
    
    review_fun=reviews(id)

    data={'brand':brand,
         'name':name,
         'images':images,
         'id':id,
        #  'Specifications':Specifications,
        #  'CompleteTheLook':CompleteTheLook,
         'rating':rating,
         'totalCountraiting':totalCountraiting,
         'userName':userName,
         'review':reviewUser,
         }
    data.update(sp)
    return data

all_Data=[]
pro_Link=[]
def crawl_list(url):
    # url='https://www.myntra.com/men-tshirts'
   
    next_page=url
    while next_page:
        r=s.get(next_page)
        soup=bs(r.text,'html.parser')
        link=re.findall('"landingPageUrl":"(.*?)",',r.text.replace('u002F','').replace('\\','/'))
        for l in link:
            links='https://www.myntra.com/'+l
            pro_Link.append(links)
            detail=crawl_detail(links)
            d={'links':links}
            d.update(detail)
            all_Data.append(d)
        if soup.find('link',attrs={'rel':'next'}):
            next_page=soup.find('link',attrs={'rel':'next'}).get('href')
            print(f'THIS IS NEXT PAGE.. {next_page}.......................')
        else:
            next_page=False



url='https://www.myntra.com/rain-jacket'
crawl_list(url)
# reviews(url)

df=pd.DataFrame(allreview)
df.to_excel('reviews.xlsx',index=False)

df=pd.DataFrame(all_Data)
df.to_excel('Myntra.xlsx',index=False)
print(all_Data)

