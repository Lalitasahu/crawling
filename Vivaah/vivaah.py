import requests
import pandas as pd 
from requests import Session
from bs4 import BeautifulSoup as bs
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'


def crawl_detail(url):
    r = s.get(url)
    soup = bs(r.text, 'html.parser')

    try:
        image = soup.find('a','center-block').find('img').get('src')
    except:
        image = ''
    
    try:
        value = [i.text for i in soup.find('div','text-left').find_all('span')]
    except:
        value = ''
    
    try:
        key = [j.text for j in  soup.find('div','text-left').find_all('li')]
    except:
        key = ''
    
    try:
        basic_info = dict(zip(key,value))
    except:
        basic_info = ''
    
    try:
        Matrimonial_Service = soup.find('div','col-xs-12 col-md-5 center-block').text.strip()
    except:
        Matrimonial_Service = ''

    try:
        text = [t.text.strip() for t in soup.find_all('div','prof_data_cont col-xs-12 col-sm-12 col-md-12')]
    except:
        text = ''

    try:
        a = [i.text for i in soup.find_all('h4','prof_sub_head fbold')]
    except:
        a = ''
    
    try:
        b = [i.text for i in soup.find_all('div','prof_sub_head fbold')]
    except:
        b = ''

    a.extend(b)
    try:
        all_info = dict(zip(a,text))
    except:
        all_info = ''
    
    # de = all_info['Family Details ']

    data = {
        'basic_info':basic_info,
        'Matrimonial_Service':Matrimonial_Service,
        'all_info': all_info,
        'image':image

    }
    return data



def crwal_lilst(url):
    category = url.split('-')[0].split('/')[-1]
    url =  f'https://www.vivaah.com/matrimonials/{category}-matrimonial.php' 
    r = s.get(url)
    print(r,r.url)
    soup = bs(r.text,'html.parser')
    single_per = soup.find_all('div','col-xs-12 col-md-9')
    for single in single_per:
        try:
            id = single.find('a').text
        except:
            id = ''
        
        try:
            p_link = 'https://www.vivaah.com'+single.find('a').get('href')
        except:
            p_link = ''
        detail = crawl_detail(p_link)

        data = {
            'landing_url':r.url,
            'id':id,
            'p_link': p_link
        }
        data.update(detail)
        print(data)
        all_profile.append(data)
all_profile = []
url = 'https://www.vivaah.com/matrimonials/punjabi-matrimonial.php'
crwal_lilst(url)
df = pd.DataFrame(all_profile)
df.to_excel('single.xlsx',index=False)

# https://www.vivaah.com/matrimony-search/bycommunity.php
# https://www.vivaah.com/matrimony-search/matrimonial_profiles_by_profession.php
# https://www.vivaah.com/matrimony-search/byreligioncaste.php
# https://www.vivaah.com/partner_search/keyword.php

# https://www.vivaah.com/partner_search/photomatrimonialprofiles.php

