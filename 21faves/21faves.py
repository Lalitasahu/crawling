import requests
import re
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import Session
s=Session()

cookies = {
    'client_id': '1668404369781181',
    '_c_id': '1668404369781824986',
    'store_locale': 'en-US',
    'shoplazza_source': '%7B%22%24first_visit_url%22%3A%22https%3A%2F%2Fwww.21faves.com%2F%22%2C%22%24latest_referrer_host%22%3A%22Google%22%2C%22expire%22%3A1669009097041%7D',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218474a53da1105-03742135b8814d-c535426-1327104-18474a53da215e%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22%24device_id%22%3A%2218474a53da1105-03742135b8814d-c535426-1327104-18474a53da215e%22%7D',
    '_ga': 'GA1.2.1588385735.1668404298',
    '_gid': 'GA1.2.1874194473.1668404298',
    '_identity_cart': 'ca635579-21f8-4776-b8da-ba7823ed6297',
    '_fbp': 'fb.1.1668404299144.84324404',
    '_identity_popups': 'aeba1e1f-799e-40ab-8395-d2bfee3b2d051668404373',
    '_identity_popups_bundle': 'f1fda628-c59a-4f08-befc-0b24b5192bf31668404373',
    '__cf_bm': 'hvknI3fb8hR2P5jddXMO_aIdifGG.Yng4NksmCHNesc-1668473918-0-AbJckDa2NvckD0LwpoTJ+QMtcBNidTwuCo3dZLghVErv2Qaae3qH/uZh2A5ol1fNN+Aqicuoyo3paNuG9eWgszo=',
    'session_id': '1668472324017256',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'Alt-Used': 'www.21faves.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.21faves.com/collections/one-pieces?spm=..index.products_1.1',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'client_id=1668404369781181; _c_id=1668404369781824986; store_locale=en-US; shoplazza_source=%7B%22%24first_visit_url%22%3A%22https%3A%2F%2Fwww.21faves.com%2F%22%2C%22%24latest_referrer_host%22%3A%22Google%22%2C%22expire%22%3A1669009097041%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218474a53da1105-03742135b8814d-c535426-1327104-18474a53da215e%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22%24device_id%22%3A%2218474a53da1105-03742135b8814d-c535426-1327104-18474a53da215e%22%7D; _ga=GA1.2.1588385735.1668404298; _gid=GA1.2.1874194473.1668404298; _identity_cart=ca635579-21f8-4776-b8da-ba7823ed6297; _fbp=fb.1.1668404299144.84324404; _identity_popups=aeba1e1f-799e-40ab-8395-d2bfee3b2d051668404373; _identity_popups_bundle=f1fda628-c59a-4f08-befc-0b24b5192bf31668404373; __cf_bm=hvknI3fb8hR2P5jddXMO_aIdifGG.Yng4NksmCHNesc-1668473918-0-AbJckDa2NvckD0LwpoTJ+QMtcBNidTwuCo3dZLghVErv2Qaae3qH/uZh2A5ol1fNN+Aqicuoyo3paNuG9eWgszo=; session_id=1668472324017256',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

params = {
    'page': '4',
    'sort_by': 'manual',
    'limit': '48',
    'tags': '',
    'price': '',
}

def crawl_detail(url):
    r=s.get(url)
    soup=bs(r.text,'html.parser')
    tables = soup.find_all('table')
    for table in tables:
        for tr in table.find_all('tr'):
            description=tr.text
    images=soup.find_all('div','swiper-slide')
    for img in images:
        image='https:'+img.find('img').get('data-src').replace('{width}','720')



    return {
        'description':description,
        'image':image

    }
all_data=[]
def crawl_list():
    total=628//48
    for page in range(total+1):
        url='https://www.21faves.com/collections/one-pieces?spm=..index.products_1'
        r=s.get(url)
        soup=bs(r.text,'html.parser')
        pro_id=re.search('"resource_id":"(.*?)"',r.text).group(1)
        api_url=f'https://www.21faves.com/api/collections/{pro_id}/products?page=4&sort_by=manual&limit=48&tags=&price='
        r=s.get(api_url,params=params, cookies=cookies, headers=headers)
        js=r.json()
        link=js['data']['products']
        for i in link:
            pro_link='https://www.21faves.com'+i.get('url')
            detail=crawl_detail(pro_link)
            print(pro_link)
            d={'pro_link':pro_link,
                'pro_id':pro_id,
                'description':detail['description'],
                'image':detail['image']
                }
            all_data.append(d)
crawl_list()
df=pd.DataFrame(all_data)
df.to_excel('121faves.xlsx',index=False)
print(all_data)


