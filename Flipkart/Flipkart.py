import pandas as pd
import requests
import csv
from bs4 import BeautifulSoup as bs
from requests import Session
s=Session()
s.headers["User-agent"]='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

xl=csv.writer(open('Flipkart.csv','w',newline=''))
xl.writerow(['Landing','name','link'])


def detailpage(url):
    r = s.get(url)
    print(r)
    soup = bs(r.text,'html.parser')
    Name_detailpage = soup.find('span','B_NuCI').text
    bread = soup.find('div',"_1MR4o5").find_all('a','_2whKao')
    breadcrums = []
    for i in bread:
        breadcrums.append(i.text)
    Brand = soup.find('span','G6XhRU').text.strip()
    selling_price = soup.find('div','_30jeq3 _16Jk6d').text
    list_price = soup.find('div','_3I9_wc _2p6lqe').text #crows price 
    Off = soup.find('div','_3Ay6Sb _31Dcoz pZkvcx').text
    star = soup.find('div','_3LWZlK _3uSWvT').text
    rating_review = soup.find('span','_2_R_DZ').text
    offer = soup.find_all('span','_3j4Zjq row')
    offers =[]
    for o in offer:
        offers.append(o.text)
    Brand_img = soup.find('div','_3nWYNs').find('img').get('src')
    aboutbrand = soup.find('div','XcYV4g').text
    service = soup.find_all('li','_2crLYm')
    services = []
    for s in service:
        services.append(i.text)
    # images='||'.join([image.find('a').get('href') for image in soup.find('ol','css-1ui811p').find_all('li','css-h5sk3m')])
    seller_name = soup.find('div','_1RLviY').text
    available = '||'.join([a.text for a in soup.find('ul','_2-RJLI').find_all('li')])
    Product_Details = []
    for i in soup.find('div','X3BRps').find_all('div','row'):
        kk = i.find('div','col col-3-12 _2H87wv').text
        vv = i.find('div','col col-9-12 _2vZqPX').text
        details ={kk:vv}
        Product_Details.append(details)
    images = '||'.join([p.find('img').get('src') for p in soup.find('ul','_3GnUWp').find_all('li')])
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
                dd = detailpage(link)
                d={
                'Landingpage':nextpage,            
                'name':name,
                'link':link
                }
                d.update(dd)
                print(d)
                xl.writerow(d.values())
                alldata.append(d)
                
            link = soup.find_all('a','_1LKTO3')
            for i in link:
                if i.text == 'Next':
                    nextpage = 'https://www.flipkart.com'+i.get('href')
                    # break
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
url = 'https://www.flipkart.com/watches/titan~brand/pr?sid=r18&otracker=nmenu_sub_Men_0_Titan&page=1'
# url = 'https://www.flipkart.com/wearable-smart-devices/smart-glasses/pr?sid=ajy%2Ctcy&otracker=nmenu_sub_Sports%2C+Books+%26+More_0_Smart+Glasses%28VR%29&otracker=nmenu_sub_Sports%2C+Books+%26+More_0_Smart+Glasses+%28VR%29&page=1'
listpage(url)
df=pd.DataFrame(alldata)
df.to_excel('Flipkart_smart_glasses.xlsx')
print(alldata)

# l.append(link)
            # r=s.get('https://www.flipkart.com'+link)
            # detailsoup=bs(r.text,            # for i in bread:
            #     brd=i.text
            #     brds.append(brd)
            #     b='||'.join(brds)
            # offer=soup.findAll('span','_3j4Zjq row')
            # for i in soup.findAll('li','_16eBzU col'):
            # # [i.text for i in soup.findAll('li','_16eBzU col')]
            #     print(i.text)