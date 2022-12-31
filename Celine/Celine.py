import requests 
import re
import pandas as pd
from lxml import html
from requests import Session
from bs4 import BeautifulSoup as bs
s =  Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'



import requests

cookies = {
    'GlobalE_Data': '%7B%22countryISO%22%3A%22IN%22%2C%22cultureCode%22%3A%22en-GB%22%2C%22currencyCode%22%3A%22INR%22%2C%22apiVersion%22%3A%222.1.4%22%7D',
    'sid': 'lc7nFs3WC68TaR5DvEOcKzX7vIkCF5lWLQo',
    'dwanonymous_e5c2d5541afa4594fef9bc36eb00fbf4': 'bcpohiJZzk5OjO3w8aKhfnw97j',
    'celine_cookies_accepted': '1',
    'mm_glc': 'AC',
    '__cq_dnt': '1',
    'dw_dnt': '1',
    'dwsid': 'sS7bw5Ha1LWrO3_o0-0mzBEbgFxeG0ZMlViENvwbpjZKW4HYgjkYwbYzYGeshK-MJIMdu680qdbUUUQCcranlw==',
    'GlobalE_CT_Data': '%7B%22CUID%22%3A%22883014952.168941534.717%22%2C%22CHKCUID%22%3Anull%7D',
    'GlobalE_Ref': 'https%3A//www.google.com/',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Dec+29+2022+11%3A24%3A27+GMT%2B0530+(India+Standard+Time)&version=6.28.0&isIABGlobal=false&hosts=&consentId=0dca6a26-69f1-4d21-8150-23a5d2ef6914&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&geolocation=IN%3BDL&AwaitingReconsent=false',
    'GlobalE_Welcome_Data': '%7B%22showWelcome%22%3Afalse%7D',
    'GlobalE_Full_Redirect': 'false',
    'OptanonAlertBoxClosed': '2022-12-29T05:36:10.609Z',
    '_ga_MENM2C5E1Q': 'GS1.1.1672292171.1.1.1672293273.0.0.0',
    '_ga': 'GA1.1.899566200.1672292171',
    '_cs_c': '0',
    '_cs_id': '0c7be083-4662-a153-ad75-1fa769ebc037.1672292171.1.1672293267.1672292171.1.1706456171344',
    '_cs_s': '6.6.0.1672295069040',
    '_gcl_aw': 'GCL.1672292284.EAIaIQobChMI7LqPoY6e_AIVyjArCh3k1QyrEAAYASAAEgKR7PD_BwE',
    '_gcl_au': '1.1.475612505.1672292172',
    'site24x7rumID': '6728256320629251.1672292148612.1672292280520',
    '_tt_enable_cookie': '1',
    '_ttp': 'ewp5fMDzSodkPX8SnQzVxrwcVK8',
    '_scid': '8b6e9cdc-7e00-4cd6-9c8e-2e2e818fa7d2',
    '_gid': 'GA1.2.133560483.1672292173',
    '_gac_UA-12251584-13': '1.1672292283.EAIaIQobChMI7LqPoY6e_AIVyjArCh3k1QyrEAAYASAAEgKR7PD_BwE',
    '_sctr': '1|1672252200000',
    '_hjSessionUser_1732248': 'eyJpZCI6IjU4OTI1M2IzLTEzMjgtNTc4Zi05ZDFkLTY0MmY5YjNkODI3NSIsImNyZWF0ZWQiOjE2NzIyOTIxNzQwMTQsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample': '0',
    '_hjSession_1732248': 'eyJpZCI6IjZkMTlmZDIxLTM5ZWQtNGRjNC04M2VlLTZmNWVlNmFkNjI4ZCIsImNyZWF0ZWQiOjE2NzIyOTIxNzQwMjYsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjIncludedInPageviewSample': '1',
    '_hjAbsoluteSessionInProgress': '0',
    '_fbp': 'fb.1.1672292174411.936646220',
    'AKA_A2': 'A',
    '_gat__ga': '1',
    '_uetsid': 'b476f9c0873a11edafdca370b53fcbd8',
    '_uetvid': 'b4770be0873a11ed9e034b98f7330bb1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    # 'Referer': 'https://www.celine.com/en-in/celine-holiday-gifts/all-gifts/hand-picked-gifts/',
    # 'Cookie': 'GlobalE_Data=%7B%22countryISO%22%3A%22IN%22%2C%22cultureCode%22%3A%22en-GB%22%2C%22currencyCode%22%3A%22INR%22%2C%22apiVersion%22%3A%222.1.4%22%7D; sid=lc7nFs3WC68TaR5DvEOcKzX7vIkCF5lWLQo; dwanonymous_e5c2d5541afa4594fef9bc36eb00fbf4=bcpohiJZzk5OjO3w8aKhfnw97j; celine_cookies_accepted=1; mm_glc=AC; __cq_dnt=1; dw_dnt=1; dwsid=sS7bw5Ha1LWrO3_o0-0mzBEbgFxeG0ZMlViENvwbpjZKW4HYgjkYwbYzYGeshK-MJIMdu680qdbUUUQCcranlw==; GlobalE_CT_Data=%7B%22CUID%22%3A%22883014952.168941534.717%22%2C%22CHKCUID%22%3Anull%7D; GlobalE_Ref=https%3A//www.google.com/; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Dec+29+2022+11%3A24%3A27+GMT%2B0530+(India+Standard+Time)&version=6.28.0&isIABGlobal=false&hosts=&consentId=0dca6a26-69f1-4d21-8150-23a5d2ef6914&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&geolocation=IN%3BDL&AwaitingReconsent=false; GlobalE_Welcome_Data=%7B%22showWelcome%22%3Afalse%7D; GlobalE_Full_Redirect=false; OptanonAlertBoxClosed=2022-12-29T05:36:10.609Z; _ga_MENM2C5E1Q=GS1.1.1672292171.1.1.1672293273.0.0.0; _ga=GA1.1.899566200.1672292171; _cs_c=0; _cs_id=0c7be083-4662-a153-ad75-1fa769ebc037.1672292171.1.1672293267.1672292171.1.1706456171344; _cs_s=6.6.0.1672295069040; _gcl_aw=GCL.1672292284.EAIaIQobChMI7LqPoY6e_AIVyjArCh3k1QyrEAAYASAAEgKR7PD_BwE; _gcl_au=1.1.475612505.1672292172; site24x7rumID=6728256320629251.1672292148612.1672292280520; _tt_enable_cookie=1; _ttp=ewp5fMDzSodkPX8SnQzVxrwcVK8; _scid=8b6e9cdc-7e00-4cd6-9c8e-2e2e818fa7d2; _gid=GA1.2.133560483.1672292173; _gac_UA-12251584-13=1.1672292283.EAIaIQobChMI7LqPoY6e_AIVyjArCh3k1QyrEAAYASAAEgKR7PD_BwE; _sctr=1|1672252200000; _hjSessionUser_1732248=eyJpZCI6IjU4OTI1M2IzLTEzMjgtNTc4Zi05ZDFkLTY0MmY5YjNkODI3NSIsImNyZWF0ZWQiOjE2NzIyOTIxNzQwMTQsImV4aXN0aW5nIjp0cnVlfQ==; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_1732248=eyJpZCI6IjZkMTlmZDIxLTM5ZWQtNGRjNC04M2VlLTZmNWVlNmFkNjI4ZCIsImNyZWF0ZWQiOjE2NzIyOTIxNzQwMjYsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1672292174411.936646220; AKA_A2=A; _gat__ga=1; _uetsid=b476f9c0873a11edafdca370b53fcbd8; _uetvid=b4770be0873a11ed9e034b98f7330bb1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}




def detailpage(url):
    r = s.get(url)
    soup = bs(r.text, 'html.parser')
    breadcrumb = soup.find('div','m-breadcrumb__items').find_all('a')
    for i in breadcrumb:
        bread = i.text

    price_detail = soup.find('strong','f-body--em').text.strip()
    description = soup.find('div','a-text f-body').text.strip()
    color = soup.find('button','m-form-dd__trigger a-btn a-btn--as-link').text.replace('\ncolor\n','').replace('\n','')
    info = soup.find('div','content-asset').find_all('p')
    for j in info:
        Availblity = j.text

    images = soup.find_all('li','m-thumb-carousel__item m-thumb-carousel__item--half-width')
    image = []
    for im in images:
        img = im.find('img').get('data-src-zoom')
        image.append(img)
    
    data = {
        'breadcrumb':bread,
        'price_detail':price_detail,
        'description':description,
        'color':color,
        'Availblity':Availblity,
        'image':image
    }
    return data

alldata = []
def listPage(url):
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    id = soup.find('button','a-btn a-btn--secondary').get('data-href')
    cgid = id.split('cgid=')[1]
    start = 20
    while True :
        params = {
        'cgid': cgid,
        'start': str(start),
        'sz': '20',
        'selectedUrl': f'https://www.celine.com/on/demandware.store/Sites-CELINE_XBAC-Site/en_IN/Search-UpdateGrid?cgid={str(cgid)}&start={start}&sz=20',
        }

        response = requests.get(
            'https://www.celine.com/on/demandware.store/Sites-CELINE_XBAC-Site/en_IN/Search-UpdateGrid',
            params=params,
            cookies=cookies,
            headers=headers,
        )

        soup = bs(response.text,'html.parser')
        products = soup.find_all('li','o-listing-grid__item')
        if products :
            for product in products:
                name = product.find('div','m-product-listing__meta-title f-body').text.replace('\n; Tan','').replace('\n','')
                Pro_link = 'https://www.celine.com'+product.find('a').get('href')
                price = product.find('strong','f-body--em').text.strip()
                detaitl = detailpage(Pro_link)
                print(name)
                
                data = {
                    'Name':name,
                    'Pro_link':Pro_link,
                    'Price':price
                }
                data.update(detaitl)
                print(data)
                alldata.append(data)
        else:
            break
        print(start)
        start += 20

        
# url = 'https://www.celine.com/en-in/celine-shop-women/ready-to-wear/jackets-and-coats/'
url = 'https://www.celine.com/en-in/celine-shop-men/ready-to-wear/denim/'
listPage(url)
df = pd.DataFrame (alldata)
df.to_excel('Celine1.xlsx',index=False)