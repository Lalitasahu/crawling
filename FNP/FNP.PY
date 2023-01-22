import requests 
import re
from bs4 import BeautifulSoup as bs
from requests import Session
import pandas as pd
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

def crwal_detail(url):
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    try:
        D_name = soup.find('div','price-with-name-desktop_productContent__2EEx_').text
    except:
        D_name = ''

    try:        
        D_price = soup.find('div','price-with-name-desktop_productPrice__1tDCN').text # only integer output ₹4,349Offers available\
    except:
        D_price = ''

    try:
        all = soup.find_all('div','product-desc-desktop_descriptionTitle__2Q-Ha')
    except:
        all = ''
    # sub_des = [i.find_all('p') for i in all]
    # for sub in sub_des:
    #     for sub_text in sub:
    #         des = sub_text.text
    #         bult_head = all.find('b')
    #         for b in bult_head:
    #             bult = b.text

    try:
        heading = [i.text for i in soup.find('div','product-desc-desktop_productDescription__1hRLx').find_all('h4')]
    except:
        heading = ''
    
    try:
        text = [ j.text for j in all]
    except:
        text = ''
    info = dict(zip(heading,text))
    try:
        Description = info['Description']
    except:
        Description = ''

    try: 
        Delivery_Information = info['Delivery Information']
    except:
        Delivery_Information = ''

    try:
        Care_Instructions = info['Care Instructions']
    except:
        Care_Instructions = ''

    data ={
        'D_name':D_name,
        'D_price':D_price,
        'Description':Description,
        'Delivery_Information':Delivery_Information,
        'Care_Instructions':Care_Instructions
    }
    return data





allproducts = []
def crwal_list(url):
    url = row['link']
    r = s.get(url)
    catlogID = url.split('?')[-1]
    slug1 = re.search('"slug1":"(.*?)",',r.text).group(1)
    categoryID = re.search('"categoryId":"(.*?)",',r.text).group(1)
    sortFields = re.search('"sortFields":"(.*?)",',r.text).group(1)
    index = 1
    nextpage = True
    while nextpage:
        api = f'https://www.fnp.com/d/control/getProductListForPlp?isMobile=false&viewIndex={index}&viewSize=40&catalogId={catlogID}&slug1={slug1}&sortFields={sortFields}&categoryId={categoryID}&earliestDatesRequired=N'
        r = s.get(api)
        soup = bs(r.text,'html.parser')
        js = r.json()
        
        if js['data']['startRows'] <= js['data']['listSize']:
            print(f'.....................{api}..............................')
            products = js['data']['productResults']
            for product in range(len(products)):
                try:
                    Name = products[product].get('productName')
                except:
                    Name = soup.find('a','product-card_card-container__1oJLc').get('title')
                
                try:
                    pro_url = 'https://www.fnp.com'+products[product].get('url')
                except:
                    pro_url = 'https://www.fnp.com'+soup.find('a','product-card_card-container__1oJLc').get('href')
                
                try:
                    image = products[product].get('productImage').get('path')
                except:
                    image = 'https://www.fnp.com'+soup.find('a','product-card_card-container__1oJLc').find('img').get('src')
                try:
                    productId = products[product].get('productId')
                except: 
                    productId = ''
                
                try:
                    price = products[product].get('price').get('price')
                except:
                    price = soup.find('a','product-card_card-container__1oJLc').find('span',{'itemprop':'price'}).text
                # print(Name)
                
                detail = crwal_detail(pro_url)
                data = {
                    'landingUrl':row['link'],
                    'Name':Name,
                    'pro_url':pro_url,
                    'image':image,
                    'productId':productId,
                    'price':price,
                    'page_rank': index,
                    'product_rank': product
                }
                data.update(detail)
                print(data)
                allproducts.append(data)

            else:
                break
    
df = pd.read_excel('Urls_FNP.xlsx')
for i in range(len(df)):
# for i in range(2):
    row = df.iloc[i].to_dict()
    crwal_list(row)


# urls = 'https://www.fnp.com/canada/all-gifts?promo=canada_giftsmenu_dt_hm' #india 
# urls = 'https://www.fnp.com/canada/gifts/vancouver?promo=canada_citiesmenu_dt_hm'    
# crwal_list(urls)
df = pd.DataFrame(allproducts)
df.to_excel('FNP_all.xlsx',index=False)
