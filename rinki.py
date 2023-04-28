# import requests 
# import time 
# import csv
# from requests import Session
# from bs4 import BeautifulSoup as bs
# import pandas as pd
# import concurrent.futures
# #url=https://bluebungalow.com.au/collections/dresses/page_2/?&rows=30

# s = Session()
# s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Language': 'en-US,en;q=0.5',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Origin': 'https://bluebungalow.com.au',
#     'Connection': 'keep-alive',
#     'Referer': 'https://bluebungalow.com.au/',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'cross-site',
#     # Requests doesn't support trailers
#     # 'TE': 'trailers',
# }

# response = requests.get(
#     'https://search.unbxd.io/ac541912a18c803bfeab27f04ccbebf4/prod-bluebungalow-au4941591590495/category?&rows=30&p=categoryPath%3A%22dresses%22&format=json&view=grid&start=30&stats=price&fields=title,uniqueId,collection_tag,plain_tags,publishedAt,secondaryImageUrl,documentType,imageUrl,price,sellingPrice,priceMax,sku,imageUrl,sizeMap,relevantDocument,productUrl,variantId,brand,availability,altImageUrl,altImageTag,imageList&facet.multiselect=true&pagetype=boolean&version=V2&indent=off&filter=documentType:product&filter=publishedAt:*&device-type=Desktop&unbxd-url=https%3A%2F%2Fbluebungalow.com.au%2Fcollections%2Fdresses%2F%3F%26rows%3D30&unbxd-referrer=&user-type=new&api-key=ac541912a18c803bfeab27f04ccbebf4',
#     headers=headers,
# )

# response
# pro=response.json()


    
# #pro.keys()
# #pro[ 'response'].keys()
# #pro[ 'response']['products'][0].keys()
# #pro[ 'response']['products'][0]['uniqueId']
# #pro[ 'response']['products'][0]['title']
# #pro[ 'response']['products'][0]['imageList']
# #pro[ 'response']['products'][0]['productUrl']
# alldata=[]

# product=pro[ 'response']['products']
# for item in product:
#     pro_id=item.get('uniqueId')
#     title=item.get('title')
#     brand=item.get('brand')
#     imageList=item.get('imageList')
#     link='https://bluebungalow.com.au'+item.get('productUrl')
#     availability=item.get('availability')
#     price=item.get('price')
#     date=item.get('publishedAt')


#     data = {
#        # 'landingPage':row['SubUrl'],
#        # 'main_api_url':url,
#         'pro_id':pro_id,
#         'link':link,
#         'title':title,
#         'brand':brand,
#         'date':date,
#         'availability':availability,
#          'price':price,
#          'imageList':imageList
#            }
#     print(data)
#     alldata.append(data)
# df = pd.DataFrame(alldata)
# df.to_excel('list2222.xlsx',index=False)   




import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import Session
s=Session()
s.headers['User-Agent']= "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0" 
alldata=[]
def allurl():
    url='https://bluebungalow.com.au/collections/dresses'
    r=s.get(url)
    soup=bs(r.text,'html.parser')
    for i in  soup.find('ul','top-navigation').find_all('li','header__parent-link level0 level-top parent'):
        if i.find('a').get('href'): #main parent url
           suburl=i.find('a').get('href')
        else: 
            suburl=''
        print(suburl)
   # for j in soup.find('ul','level0').find_all('li'):
    #    category=j.find('a').get('href')
     #   print(category)    

    # for k in soup.find('ul','level0').find_all('li','level1 item'):
    #     if k.find('a').get('href'):
    #        cat=k.find('a').get('href')
    #        print(cat)
    #     else:
    #         cat=''   


        # data ={ 'suburl':suburl,
        #     #S  'category' :category
        #        'cat' : cat
        #         }
            
                
        # alldata.append(data)
        # print(data)
allurl()   
# df = pd.DataFrame(alldata)
# df.to_excel('blue_final4444.xlsx',index=False)