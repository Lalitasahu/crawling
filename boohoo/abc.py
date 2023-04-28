import requests
import json
import time
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from requests import Session 
import concurrent.futures
s = Session()

# s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
# url = 'https://www.boohoo.com/mens/new-in'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': 'text/html',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.boohoo.com/mens/no-referrer',
    'Connection': 'keep-alive',
    # 'Cookie': 'dwanonymous_3c96516478c33a12ebf223e921102926=ab9U4BH6Sg2kzPSilXWf9cV95T; countryBannerStatus=open; forterToken=eea233dc21794fcdb688bc1b15888352_1674451873096__UDF43_9ck; ftr_ncd=6; ABTasty=uid=t3w93745qm0mv70e&fst=1674384436422&pst=1674439142720&cst=1674451187721&ns=5&pvt=110&pvis=9&th=881725.1098305.13.13.1.1.1674387201242.1674441317116.1.4_882756.1099564.13.13.1.1.1674387201388.1674441319149.1.4_883379.1100341.13.13.1.1.1674387201531.1674441322201.1.4_883445.1100451.95.57.3.1.1674384547028.1674451875875.1.5_899833.1121822.13.13.1.1.1674387201234.1674441324223.1.4_927156.1157117.81.54.3.1.1674384547029.1674451875881.1.5_927157.1157115.13.13.1.1.1674387201559.1674441329282.1.4; __exponea_etc__=9d6ba457-9e36-4253-bf5c-c867cc34c820; cd_user_id=185d916f2a7705-074f9a9a764aca-c5c5429-144000-185d916f2a8600; C360i=F27C37C935716E2B47BA03D99770363D|eyJjcmVhdGVkIjoxNjc0Mzg0NDM4NjcwLCJ1cGRhdGVkIjoxNjc0NDUxODc3NDU5LCJ0YWdfaWQiOiI0LjMuMCIsImNvdW50Ijo4OSwiZXhwIjoxNzA1OTIwNDM4NjcwfQ==; _attn_=eyJ1Ijoie1wiY29cIjoxNjc0Mzg0NDM4NzIzLFwidW9cIjoxNjc0Mzg0NDM4NzIzLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImU2NDk0MzI3YmFkYjQ3ZTBhOTJlY2QxNGFlYTRjNzkyXCJ9In0=; tpc_a=814abadbd35e4a318c13bb46832a0730.1674384438.g3t.1674451190; __attentive_id=e6494327badb47e0a92ecd14aea4c792; __attentive_cco=1674384438751; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2NzQzODQ0MzksInZhbHVlIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuYm9vaG9vLmNvbS8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2NzQ0NTE4NzgsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmJvb2hvby5jb20vIn19; __attentive_dv=1; dw_country_locale=en_GB; dw_cookies_accepted=A; dw_consent_cookie=B; dw_is_new_consent=true; _ga=GA1.2.384781377.1674384438; _gid=GA1.2.627284764.1674384455; _gcl_au=1.1.1250552778.1674384455; __adal_first_visit=1674384455539; __adal_session_start=1674451189374; __adal_last_visit=1674451877061; syte_uuid=2ecbca60-9a42-11ed-aeb6-99737d4e0888; _scid=1a559b14-5c7f-408b-8aa6-247c3b265045; PERSONIFY=1674384456290-fce20afe-d1ed-b899-2e44-fa30c601bcd1; _cs_ex=1499948428; _cs_c=1; _rl_rl=0; _rlgm=54|y|4yfwPMMN|c229:y/x6o2V4nKn:y/c334:y/c335:y/lRpOl8BkV:y/ywX0qElDR:y/Rl1RZYZ0q:y/57W7ZvPwA:y/x6l6M0mwJ:y/jYnrJNK55:y/vQmJj2GlM:y/gpkBVqgD6:y/EqZZ7v4Wl:y/DqYY2m5Dk:y/ZN39V1z8:y/mq2xrwoB3:y/qQVByMPBG:y/yw6Voy3gP:y/GRw65jv95:y/NO7k9q5qp:y|; _rlu=6d2c83fb-ad9b-4be6-abed-5f35643b8fcc; _rll_c_229_d=1674393811573; _rll_c_229_c=0; _rll_c_234_d=1674384459733; _rll_c_234_c=1; _rll_c_922_d=1674384456743; _rll_c_922_c=0; _sctr=1|1674325800000; _pin_unauth=dWlkPVpEUXdZalU1TUdNdFpqSTBPQzAwTVRneExUZ3dZV0V0Tm1ZeE16VTVNekprTTJOag; _tt_enable_cookie=1; _ttp=Ooi3-k9pFl8eCHbSwQTedYitwtU; _hjSessionUser_614554=eyJpZCI6ImYwNmJiNDE4LWM5MzQtNTgzZC1hNGJkLTY4MGNmZmE2MWZkMyIsImNyZWF0ZWQiOjE2NzQzODQ0NTg3NTIsImV4aXN0aW5nIjp0cnVlfQ==; _fbp=fb.1.1674384459203.1462002425; _ga_CKX55DLD7G=GS1.1.1674451186.6.1.1674451885.47.0.0; __cq_uuid=ab9U4BH6Sg2kzPSilXWf9cV95T; __cq_seg=0~-0.03!1~-0.30!2~0.37!3~-0.05!4~-0.25!5~0.73!6~-0.16!7~0.00!8~0.26!9~-0.29!f0~15~5; _rll__sel1m_d=1674451618244; _rll__sel1m_c=2; __cq_bc=%7B%22bbvc-boohoo-UK%22%3A%5B%7B%22id%22%3A%22PREMIER%22%7D%2C%7B%22id%22%3A%22GZZ39623%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22GZZ39623-2%22%7D%2C%7B%22id%22%3A%22GZZ38755%22%7D%2C%7B%22id%22%3A%22GZZ47400%22%7D%2C%7B%22id%22%3A%22BMM37919%22%7D%2C%7B%22id%22%3A%22BMM22402%22%2C%22sku%22%3A%22BMM22402-265-30%22%7D%2C%7B%22id%22%3A%22BMM35468%22%7D%2C%7B%22id%22%3A%22BMM33227%22%7D%2C%7B%22id%22%3A%22BMM34205%22%7D%5D%7D; personalisation_session_skus_ls={%2219300430%22:[%22undefined%22]}; _rll__sel2m_d=1674451618245; _rll__sel2m_c=2; _rll__sel5m_d=1674451618246; _rll__sel5m_c=2; _rll__sel10m_d=1674451877375; _rll__sel10m_c=2; _rll__sel30m_d=1674387145210; _rll__sel30m_c=1; _rll__sel60m_d=1674388905295; _rll__sel60m_c=1; dwac_901934c2df27fe61a1e3d786c2=Lm3SLT6l0Yog1KiYzt-OFTiEiVG-BvJEVzs%3D|dw-only|||GBP|false|Europe%2FLondon|true; cqcid=ab9U4BH6Sg2kzPSilXWf9cV95T; cquid=||; sid=Lm3SLT6l0Yog1KiYzt-OFTiEiVG-BvJEVzs; __cq_dnt=0; dw_dnt=0; dwsid=4c-kYFFM2hkCh61nRsWfNPcm_xzR7_nXdWgi4c6-QIM8JFAozkrjKgKcVO5av_8IZg6QmzuDPGjhoN79lOjmqQ==; _cs_mk_ga=0.35487099907697583_1674451186434; stimgs={%22sessionId%22:93144058%2C%22didReportCameraImpression%22:false%2C%22newUser%22:false}; sessionStarted=1; ABTastySession=mrasn=&lp=https%253A%252F%252Fwww.boohoo.com%252F; __exponea_time2__=195.55547952651978; _rllt=1674451189426; _rlsnk=6d2c_ld8d0704; __attentive_pv=9; __attentive_ss_referrer=ORGANIC; _hjIncludedInSessionSample=1; _hjSession_614554=eyJpZCI6ImIyZjQyYjZkLWY5YzktNDQwNS05MGQ0LWNhMzQ4N2ExZmJlMyIsImNyZWF0ZWQiOjE2NzQ0NTExOTIwMDIsImluU2FtcGxlIjp0cnVlfQ==; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; _rll__sel1m_sc=1; _rll__sel1m_sd=1674451618244; _rll__sel2m_sc=1; _rll__sel2m_sd=1674451618245; _rll__sel5m_sc=1; _rll__sel5m_sd=1674451618246; _dc_gtm_UA-994466-1=1; _uetsid=2edddae09a4211ed94b0e1da9a9eefe9; _uetvid=2eddd3109a4211ed9425b1b382b03eb1; _rll__sel10m_sc=1; _rll__sel10m_sd=1674451877375',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'same-origin',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

def crwal_detailpage(url):
    print(url)
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    D_name = soup.find('h1').text.strip()
    D_price = soup.find('div','b-product_details-price').find('span','b-price-item').text.strip()
    color = soup.find('span','b-variation_label-value').text.strip()
    size = soup.find('span','b-variation_swatch-value_text').text
    bread = [i.text.strip() for i in soup.find('nav','b-breadcrumbs').find_all('span')]
    product_Detail = soup.find('div','b-product_details-content').text.strip()
    Return = soup.find('div','b-product_shipping-returns_content').text.strip()
    image1 = soup.find('div',id='product_gallery_track').find('img').get('src')
    image2 = soup.find('div',id='product_gallery_track').find('img').get('src')+'_1'
    data ={
        'D_name':D_name,
        'D_price':D_price,
        'color':color,
        'size':size,
        'bread':bread,
        'product_Detail':product_Detail,
        'Return':Return,
        'image1':image1,
        'image2':image2
    }
    return data


def crwal_listpage(url):
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    # s.mount('http://', adapter)
    # s.mount('https://', adapter)
    url = row['allurl']
    rr = s.get(url, headers=headers)
    dsoup = bs(rr.text,'html.parser')
    cgid = dsoup.find('html').get('data-querystring')
    start = 40
    nextpage = True
    pageno = 1
    while nextpage:
        
        params = {
            'cgid': 'mens-suits',
            'start': str(start),
            'sz': '40',
            'selectedUrl': f'https://www.boohoo.com/on/demandware.store/Sites-boohoo-UK-Site/en_GB/Search-UpdateGrid?cgid=mens-suits&start={start}&sz=40',
            'ajax': 'true',
        }
        # api = f'https://www.boohoo.com/womens/dresses?start={start}&sz=40'
        # api = f'https://www.boohoo.com/mens/new-in?start={start}&sz=40'
        # api = f'https://www.boohoo.com/on/demandware.store/Sites-boohoo-UK-Site/en_GB/Search-UpdateGrid?{cgid}&start={start}&sz=40&selectedUrl=https://www.boohoo.com/on/demandware.store/Sites-boohoo-UK-Site/en_GB/Search-UpdateGrid?{cgid}&start={start}&sz=40&ajax=true'
        api = 'https://www.boohoo.com/on/demandware.store/Sites-boohoo-UK-Site/en_GB/Search-UpdateGrid'
        time.sleep(4)
        
        r = s.get(api, params=params, headers=headers)
        print(r.url)
        soup = bs(r.text,'html.parser')
        products = soup.find_all('section','b-product_tile')
        if products:
            for product in range(len(products)):
                Name = products[product].find('h3').find('a').text.strip()
                if 'https://www.boohoo.com':
                    pro_link = 'https://www.boohoo.com'+products[product].find('h3').find('a').get('href')
                else:
                    pro_link = products[product].find('h3').find('a').get('href')
                
                try:
                    info = json.loads(products[product].find('h3').find('a').get('data-analytics'))
                    pro_id = info['id']
                    category1 = info['category1']
                    price = '£'+info['price']
                    itemId = info['itemId']
                except:
                    info=''
                # details = crwal_detailpage(pro_link)
                data = {
                    'landingURL':row['allurl'],
                    'product_rank':product,
                    'No_of_pages':pageno,
                    'Name':Name,
                    'pro_link':pro_link,
                    'pro_id':pro_id,
                    'category1':category1,
                    'price':price,
                    'itemId':itemId,
                }
                print(data)
                alldata.append(data)
        else:
            break
        start += 40
        pageno += 1

alldata = []
products = []
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    df = pd.read_excel('allurls.xlsx')
    for i in range(len(df)):
    # for i in range(2):
        row = df.iloc[i].to_dict()
        url = row.get("allurl")
        if str(url) == 'nan' or '.html' in str(url):
            continue
        crwal_listpage(row)

df = pd.DataFrame(alldata)
df.to_excel('boohooAll.xlsx',index=False)
#     df = pd.read_excel('bluebungalow_cat_Url.xlsx')
#     for i in range(len(df)):
#     # for i in range(3):
#         row = df.iloc[i].to_dict()
#         # listpage(row)
#         executor.submit(listpage,row)


# df = pd.DataFrame(alldata)
# df.to_excel('bluebungalow_listpage.xlsx',index=False)


    # df = pd.read_excel('BlueBungalow/bluebungalow_listpage.xlsx').drop_duplicates(['pro_id'])
    # for i in range(len(df)):
    # # for i in range(2):
    #     row = df.iloc[i].to_dict()
    #     detailpage(row)

    # df = pd.DataFrame(products)
    # df.to_excel('blue14_detailpage.xlsx',index=False)
