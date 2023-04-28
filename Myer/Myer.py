import requests 
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import Session

import concurrent.futures

s=Session()
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
# url='https://www.myer.com.au/c/men/men-sleepwear/pyjamas-777611-1'



# def review(url):
#     ur_name=
#     rv_data=
#     review=
#     review_no=


def crawl_detail(url):
    r=s.get(url)
    print(url)
    soup=bs(r.text,'html.parser')
    name=soup.find('h1').text
    pro_code=soup.find('p',{'data-automation':'product-part-number'}).find('span').text
    Brand=soup.find('span',attrs={'data-automation':'product-brand-name'}).text
    price=soup.find('h3').text
    discription=soup.find('div',attrs={'id':'product-details-accordian-description-accordion-id'}).text

    images='||'.join([image.find('a').get('href') for image in soup.find('ol','css-1ui811p').find_all('li','css-h5sk3m')])
    return {
        'name':name,
        'pro_code':pro_code,
        'Brand':Brand,
        'price':price,
        'Discription':discription,
        'images':images
    }

all_Data=[]

def crawl_list(row):
    # url='https://www.myer.com.au/c/men/men-sleepwear/pyjamas-777611-1'
    url=row['url']
    next_page=url
    
    
    while next_page:
    
        r=s.get(next_page)
        # print(r.url)
        soup=bs(r.text,'html.parser')
        # next_page=soup.find('li','next disabled css-0').find('a').get('href')   #for next page url\
        products=soup.find_all('h3')
        print(len(products))
        for product in products:
            Pro_link='https://www.myer.com.au'+product.find('a').get('href')
            details=crawl_detail(Pro_link)

            data={
                'pro_link':Pro_link,
                'name':details['name'],
                'pro_code':details['pro_code'],
                'Brand':details['Brand'],
                'price':details['price'],
                'images':details['images'],
                'Discription':details['Discription'],
                'cat_url':next_page
            }
            all_Data.append(data)
            # print(data)
        if soup.find('li','next'):
            next_page='https://www.myer.com.au'+soup.find('li','next').find('a').get('href')
            print(f'NEXT PAGE.. {next_page}.......................')
        else:
            next_page = False
         



df = pd.read_excel('input_.xlsx')
for i in range(len(df)):
    row = df.iloc[i].to_dict()
    crawl_list(row)


# with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#     for i in range(len(df)):
#         row = df.iloc[i].to_dict()
#         # crawl_list(row)
#         executor.submit(crawl_list,row)



df=pd.DataFrame(all_Data)
df.to_excel('Myer1.xlsx',index=False)

print(all_Data)