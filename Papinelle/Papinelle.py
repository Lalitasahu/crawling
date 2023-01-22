import requests 
from bs4 import BeautifulSoup as bs
from requests import Session
import pandas as pd 
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'


def crwal_details(url):
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    Dprice = soup.find('p','afterpay-paragraph').find('span').text.strip()
    description = soup.find('meta',{'name':'description'}).get('content')
    image = []
    for im in soup.find('div','Product__Slideshow Product__Slideshow--zoomable Carousel').find_all('div','Product__SlideItem Product__SlideItem--image Carousel__Cell'):
        img = im.find('img').get('data-src').replace('{width}','700')
        image.append(img)
    keys = [i.text.strip() for i in soup.find('form','ProductForm').find_all('button','Collapsible__Button')]
    values = [i.text.strip() for i in soup.find('form','ProductForm').find_all('div','Collapsible__Inner')]
    info = dict(zip(keys,values))
    Description = info['Description']
    Fabic = info['Fabric']
    Fit = info['Fit']
    Shipping = info['Shipping Details']    

    data = {
        'price':Dprice,
        'description':description,
        'image':image,
        'Description':Description,
        'Fabic':Fabic,
        'Shipping':Shipping

    }
    return data
    
    

alldata = []
def crwal_list(url):
    r = s.get(url)
    print(url)
    soup = bs(r.text,'html.parser')
    # nextpage = url
    # # nextpage = True
    # while nextpage:
    total = soup.find('span',{'id':'ProductCount'}).text.replace('Products Found','').strip()
    pages = int(total)//34
    for page in range(1,pages):
        urls = url.format(page)
        r = s.get(urls)
        print(r,urls)
        soup = bs(r.text,'html.parser')
        products = soup.find_all('div','Grid__Cell 1/2--phone 1/3--tablet-and-up 1/4--lap-and-up')
        for product in products:

            try:
                name = product.find('h2').text.strip()
            except:
                name = ''
            try:
                pro_link = "https://www.papinelle.com"+product.find('h2','ProductItem__Title Heading').find('a').get('href')
            except:
                pro_link = ''

            try:
                price = product.find('span','ProductItem__Price Price Text--subdued').text
            except:
                price = ''

            try:
                promo_label = product.find('a',"ProductItem__PromoLabel Heading Text--subdued").text
            except:
                promo_label = ''
            
            try:
                list_image = product.find('a','ProductItem__ImageWrapper ProductItem__ImageWrapper--withAlternateImage').find('img').get('data-src')
            except:
                list_image = ''
            
            try:
                color = [product.text.strip() for product in soup.find('ul','ColorSwatchList HorizontalList').find_all('li')]
            except:
                color = ''
            
            try:
                detail = crwal_details(pro_link)
            except:
                detail = ''
            data = {
                'landingURL':urls,
                'name':name,
                'pro_link':pro_link,
                'price':price,
                'promo_label':promo_label,
                'list_image':list_image,
                'color':color
            }
            data.update(detail)
            print(data)
            alldata.append(data)
        # nextpage = soup.find_all('a','Pagination__NavItem Link Link--primary',{'title':"Next page"}).text
        # for i in nextpage:
        #     if nextpage == '':
        #         nextpage =  "https://www.papinelle.com"+soup.find_all('a','Pagination__NavItem Link Link--primary',{'title':"Next page"}).get('href')
        #         print(f'......................................{nextpage}..............................................')
        #         # break
        #     else:
        #         nextpage = False
            
url = 'https://www.papinelle.com/collections/womens-sleepwear?page={}'
crwal_list(url)
df = pd.DataFrame(alldata)
df.to_excel('Papinelle.xlsx',index=False)