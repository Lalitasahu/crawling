import pandas as pd
import requests
import csv
from bs4 import BeautifulSoup as bs
from requests import Session
s=Session()
s.headers["User-agent"]='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

xl=csv.writer(open('Flipkart_watch.csv','w',newline='',encoding='utf-8'))
xl.writerow(['Landing','name','link','Name_detailpage','breadcrums','Brand','selling_price','list_price','Off','Stars',
              'rating_review','offers','Brand_img','aboutbrand','services','available','Product_Details','images'])
def detailpage(url):
    r = s.get(url)
    print(r)
    soup = bs(r.text,'html.parser')
    try:
        Name_detailpage = soup.find('span','B_NuCI').text
    except:
        Name_detailpage = ''

    try:
        bread = soup.find('div',"_1MR4o5").find_all('a','_2whKao')
        breadcrums = []
        for brd in bread:
            breadcrums.append(brd.text)
    except:
            breadcrums=''

    try:
        Brand = soup.find('span','G6XhRU').text.strip()
    except:
        Brand = ''
    
    try:
        selling_price = soup.find('div','_30jeq3 _16Jk6d').text
    except:
        selling_price = ''
    
    try:
        list_price = soup.find('div','_3I9_wc _2p6lqe').text #crows price 
    except:
        list_price = ''

    try:
        Off = soup.find('div','_3Ay6Sb _31Dcoz pZkvcx').text
    except:
        Off = ''
    
    try:
        star = soup.find('div','_3LWZlK _3uSWvT').text
    except:
        star = ''

    try:
        rating_review = soup.find('span','_2_R_DZ').text
    except:
        rating_review = ''

    try:
        offer = soup.find_all('span','_3j4Zjq row')
        offers =[]
        for ofr in offer:
            offers.append(ofr.text)
    except:
            offers = ''
        
    try:
        Brand_img = soup.find('div','_3nWYNs').find('img').get('src')
    except:
        Brand_img = ''

    try:
        aboutbrand = soup.find('div','XcYV4g').text
    except:
        aboutbrand = ''
    
    try:
        service = soup.find_all('li','_2crLYm')
        services = []
        for ser in service:
            services.append(ser.text)
    except:
            services = ''

    # images='||'.join([image.find('a').get('href') for image in soup.find('ol','css-1ui811p').find_all('li','css-h5sk3m')])
    try:
        seller_name = soup.find('div','_1RLviY').text
    except:
        seller_name = ''

    try:
        available = '||'.join([avl.text for avl in soup.find('ul','_2-RJLI').find_all('li')])
    except:
        available = ''
    
    try:
        Product_Details = []
        for i in soup.find('div','X3BRps').find_all('div','row'):
            kk = i.find('div','col col-3-12 _2H87wv').text
            vv = i.find('div','col col-9-12 _2vZqPX').text
            details ={kk:vv}
            Product_Details.append(details)
    except:
            Product_Details = ''

    try:
        images = '||'.join([im.find('img').get('src') for im in soup.find('ul','_3GnUWp').find_all('li')]).replace('128','832')
    except:
        images = ''


    detail_data ={
        'Name_detailpage':Name_detailpage,
        'breadcrums':breadcrums,
        'Brand':Brand,
        'selling_price':selling_price,
        'list_price':list_price,
        'Off':Off,
        'Stars':star,
        'rating_review':rating_review,
        'offers':offers,
        'Brand_img':Brand_img,
        'aboutbrand':aboutbrand,
        'services':services,
        'seller_name':seller_name,
        'available':available,
        'Product_Details':Product_Details,
        'images':images
    }
    return detail_data


alldata=[]
def listpage(url):
    nextpage = url
    # print(nextpage) 
    while nextpage:
        print(f'................{nextpage}................')
        r=s.get(nextpage)
        # print(nextpage,r.status_code)
        soup=bs(r.text,'html.parser')
        products =soup.findAll('div','_2B099V')

        if products:  
                 
            for i in products:
                name=i.find('a','IRpwTa').text
                link='https://www.flipkart.com'+i.find('a','IRpwTa').get('href')
                detail_page= detailpage(link)
                d={
                'Landingpage':nextpage,            
                'name':name,
                'link':link
                }
                d.update(detail_page)
                print(d)

                alldata.append(d)
                xl.writerow(d.values())
                
            link = soup.find_all('a','_1LKTO3')
            for i in link:
                if i.text == 'Next':
                    nextpage = 'https://www.flipkart.com'+i.get('href')
        else:
            break
                
        
        # next = []
        # print(link)
        # for l in link:

            # next.append(l.get('href'))
            # print(next)
        
        # if len(next) == 2:
            # nextpage = 'https://www.flipkart.com'+soup.find_all('a','_1LKTO3')[1].get('href')
            # print("sdjdsjfkj",nextpage)
            # print(f'..........{nextpage}................')
  

# url = 'https://www.flipkart.com/games/ps4/pr?p%5B%5D=sort%3Dpopularity&sid=4rr%2Ctg9%2Cweu&pincode=560068&filterNone=true&otracker=nmenu_sub_Sports%2C%20Books%20%26%20More_0_PS4%20Games&otracker=nmenu_sub_Sports%2C%20Books%20%26%20More_0_PS4%20Games'
# url = 'https://www.flipkart.com/watches/titan~brand/pr?sid=r18&otracker=nmenu_sub_Men_0_Titan&page=1'
url = 'https://www.flipkart.com/wearable-smart-devices/smart-glasses/pr?sid=ajy%2Ctcy&otracker=nmenu_sub_Sports%2C+Books+%26+More_0_Smart+Glasses%28VR%29&otracker=nmenu_sub_Sports%2C+Books+%26+More_0_Smart+Glasses+%28VR%29&page=1'
listpage(url)
df=pd.DataFrame(alldata)
df.to_excel('Flipkart.xlsx')
print(alldata)
