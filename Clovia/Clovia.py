import requests
import math
import csv
from requests import Session
import pandas as pd
from bs4 import BeautifulSoup as bs
s = Session()
# s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

xl=csv.writer(open('detail_page_data_try.csv','w',newline=''),delimiter="@")
xl.writerow(['name','id','get_absolute_url','offer_tag','rounded_up_unit_price_ui','rounded_up_unit_price','rating','description','images','video'])


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Alt-Used': 'www.clovia.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.clovia.com/active-wear/gym-wear/s/',
    # 'Cookie': 'sessionid=nv6f3z9xi88aq4rtlfbmczw54jrl15u2; nur=None; http_referer_val="firstclicktime=2023-02-01 12:48:24.143476\\054http_referer=https://www.google.com/"; __cf_bm=RBHFBqbiKzTF0KhwTrSu9.gVL.SJ8d7lq4JP_3n95zw-1675235904-0-AfXg6t08boMQpWmSxhfD1deEbYGVwOiW/eQ7vdYwSEBNES09+Q1wB/RFfXjyGjJOdK5yMSxI+LYAGBhIGCgBj/c=; _cfuvid=UeTlZLIgcExdozkjO6JnSf4.a3WxCC3MLnSI_FxsIDE-1675235904154-0-604800000; _gcl_au=1.1.145706941.1675235696; _browsee=eyJfaWQiOiJjNGNiM2QwMjg4N2EiLCJfdCI6MTY3NTIzNTY5NjA4MywiX3IiOjAsIl9wIjp7ImNvIjpmYWxzZSwiZXQiOnRydWUsInByIjpbMV0sIml0IjpbXX19; _browseet=eyJfdCI6MTY3NTIzNTc3MDA5N30=; _ga_TC6QEKJ4BS=GS1.1.1675235696.1.1.1675235868.60.0.0; _ga=GA1.2.1600409455.1675235696; _gid=GA1.2.1059240923.1675235698; _clck=14wej1s|1|f8r|0; cto_bundle=v260AF9DeWdjOHhFcTI2bGVnJTJCV3JhUXBYZjFkT3FiaVVBcyUyRlNScjVTUlllUFYzWDN3YlFzQm5GTFdVeVdFUEZrVEExdVZVaHlwcjIlMkJkTDBoZTBmT0o2Wk9KQjNHY0VsaVMxZVlPbGQyNlZKUWN1SDFOODFyaDdkJTJCaHd2UE1RZ2VYSDlpN2tvSEhVNGdzYVo5eW5yWW5KT1lJZyUzRCUzRA; _fbp=fb.1.1675235698436.998948754; _clsk=1fn36fm|1675235771368|2|0|n.clarity.ms/collect; g_state={"i_p":1675242904330,"i_l":1}',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

def allUrl():
    url = 'https://www.clovia.com'
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    for i in soup.find_all('li','megaMenu'):
        all_ctg_url = 'https://www.clovia.com'+i.find('a').get('href') 
    # all_ctg_url = ['https://www.clovia.com'+i.find('a').get('href') for i in soup.find_all('li','megaMenu')]
        data = {
            'allurl':all_ctg_url
        }
        print(data)
        allcategoryUrl.append(data)


def crawal_detail(row):
    a = row['pro_url'].split('/')[-1]
    api = f'https://www.clovia.com/web/api/v1/product-desktop/{a}/'
    print(api)
    r = s.get(api)
    js = r.json()
    if js:
        name = js['name']
        id = js['id']
        get_absolute_url = 'https://www.clovia.com/product/'+js['get_absolute_url']
        offer_tag = js['offer_tag']
        rounded_up_unit_price_ui = js['rounded_up_unit_price_ui']
        rounded_up_unit_price = js['rounded_up_unit_price']
        rating = js['rating']
        description = bs(js['description']).text
        images = [i.get('img_l') for i in js['gallery']]
        video = js['gallery']
        for j in video:
            v = j.get('url')

        data = {
            'landingUrl':row['pro_url'],
            'name':name,
            'id':id,
            'get_absolute_url':get_absolute_url,
            'offer_tag':offer_tag,
            'rounded_up_unit_price_ui':rounded_up_unit_price_ui,
            'rounded_up_unit_price':rounded_up_unit_price,
            'rating':rating,
            'description':description,
            'images':images,
            'video':v
        }
        print(data)

    else:
        pass
    
    xl.writerow(data.values())
    detail_page_data.append(data)

def crawl_listpage(url):
    url = row['allurl']
    nextpage = True
    page = 1
    pro_cat = url.split('/')[3]
    cat = url.split('/')[-3]
    while nextpage:
       
        url = f'https://www.clovia.com/web/api/v1/category-products-desktop/{pro_cat}/{cat}/s/?page={page}'
        r = s.get(url,headers=headers)
        print(r.url,r)
        js = r.json()
        total = js['result']['total_count']
        if  js['result']['page'] < math.ceil(total/12):
            products  = js['result']['products']
        # if products:
            for product in products:
                name = product.get('name')
                id = product.get('id')
                pro_url = 'https://www.clovia.com/product/'+product.get('slug')
                sku = product.get('sku')
                all_size_prop = product.get('all_size_prop')
                rounded_up_unit_price = product.get('rounded_up_unit_price')
                rounded_up_unit_price_ui = product.get('rounded_up_unit_price_ui')
                old_price_ui = product.get('old_price_ui')
                # image = product.get('image').get('first_image_url')
                review_count = product.get('review_count')
                star_rating = product.get('star_rating')
                offer_tag = product.get('offer_tag')
                product_related_video = product.get('product_related_video')
                data = {
                    'landingUrl':row['allurl'],
                    'name':name,
                    'id':id,
                    'pro_url':pro_url,
                    'sku':sku,
                    'all_size_prop':all_size_prop,
                    'rounded_up_unit_price':rounded_up_unit_price,
                    'rounded_up_unit_price_ui':rounded_up_unit_price_ui,
                    'old_price_ui':old_price_ui,
                    'review_count':review_count,
                    'star_rating':star_rating,
                    'offer_tag':offer_tag,
                    'product_related_video':product_related_video
                }
                print(data)                
                list_page_data.append(data)
        else:
            nextpage =  False
            
        page += 1

allcategoryUrl = []
list_page_data = []
detail_page_data = []

df = pd.read_excel('list_page_data.xlsx').drop_duplicates(['id'])
for i in range(len(df)):
# for i in range(2):
    row = df.iloc[i].to_dict()
    crawal_detail(row)

df = pd.DataFrame(detail_page_data)
df.to_excel('detail_page_data.xlsx',index=False)

# df = pd.read_excel('allURL.xlsx')
# for i in range(len(df)):
# # for i in range(2):
#     row = df.iloc[i].to_dict()
#     crawl_listpage(row)
    
# df = pd.DataFrame(list_page_data)
# df.to_excel('list_page_data.xlsx', index= False)


# allUrl()
# df = pd.DataFrame(allcategoryUrl)
# df.to_excel('allURL.xlsx',index=False)