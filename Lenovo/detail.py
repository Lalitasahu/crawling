import requests
import csv
import re
import pandas as pd
import json
import time
from lxml import html
from bs4 import BeautifulSoup as bs
from requests import Session
import concurrent.futures
from scrapingbee import ScrapingBeeClient


xl=csv.writer(open('lenovofinalfil1.csv','w',newline='', encoding='utf-8'))
xl.writerow(['landinUrl','name','space','image','Bread','stock','price','Processor','Graphics','Display','Memory','Storage'])


c = ScrapingBeeClient(api_key='AH9282OM4DTE7BL44OODR08U6PTH08HK9NRQZDR00PA5QW3KD2XA97HI3QEIRHMXRBG52D44GF3VBBJ3')
s=Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.lenovo.com/us/en/p/laptops/thinkpad/thinkpadt/ThinkPad-T16-(16-inch-Intel)/LEN101T0017',
    # 'Referer': 'https://www.lenovo.com/us/en/p/laptops/thinkpad/thinkpadx1/thinkpad-x1-carbon-gen-10-(14-inch-intel)/len101t0009',
    'Origin': 'https://www.lenovo.com',
    'Connection': 'keep-alive',
    # 'Cookie': 'zipcode=60654; _abck=38FFA3FD8B7C4AE2FD3DB8008412743E~0~YAAQLG4/Fw185wSFAQAAO9rjuQkZ1oegpXZXg6/FyTJ5KuY6925eGXkMlIcs2jOWN+w807JAHm941xoMRpgIqngtKzqtJHw02aNbMM8levCoVb7F4sZrknMpyY59dZjGjwOWlliCGgi8WNbB20ATXIspHLDmf5j0Zf1G/sw5og8IkaKGMulIb3KtacrMCZWBFW1Z/MulMTx2lgKSi9HZ/gbkVAvP2pa2Hz4Knz2dGplhcpTjXfKqPT7Ia26mfD9q0XTWjEU76UFpY305ORDB0QVsaS0Mpv2N8Ux3S93jNsaqSEyyOd9NrBH44OdAS5JUZVxKNZvXlCjZyyHDz7QcRzJckoCEFn5EjCvlenWN06N7pNpEUOz7Xq4DGLqESXKY+VL2igumFMW2rddiYXuWOCIp7p1mr2Qo0Q==~-1~-1~1673864486; utag_main=v_id:0183b77f38160034ee27834da85405050008500d00978$_sn:3$_se:1$_ss:1$_st:1671192200838$_ga:0183b77f38160034ee27834da85405050008500d00978$dc_visit:3$ses_id:1671190400838%3Bexp-session$_pn:1%3Bexp-session$criteo_sync:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:ap-east-1%3Bexp-session; kndctr_F6171253512D2B8C0A490D45_AdobeOrg_identity=CiY2NjUxODQ4NzU3NjE0OTE5NTk0MDI1NDUyMTY1NTMxNDQzNjU5N1IRCNPH%5Fbu7MBABGAEqBElORDGgAfaSyqbbMKgBtarVzKvs8Z0T8AHp6JrO2zA%3D; AMCV_F6171253512D2B8C0A490D45%40AdobeOrg=MCMID|66518487576149195940254521655314436597; BVBRANDID=431bcd48-5c26-4b0d-a434-c7c5d1240eac; hero-session-23ba646a-b0d7-46ca-af03-cc5bf3b24d83=author=client&expires=1702726400958&visitor=7fffd157-5c93-4fc6-888c-3c772b76315c; s_tslv=1673860812376; s_vnc365=1705394904635%26vn%3D20; _ga_LXNLK45HZF=GS1.1.1673858908.20.1.1673860840.0.0.0; _ga=GA1.1.701193512.1665230916; inside-eu2=505712570-46f4011a36c4747c127723f3754c6fe6808faf042444be68a365e413af25aebe-0-0; _evidon_consent_cookie={"consent_date":"2022-10-08T12:08:36.289Z","categories":{"6":true},"vendors":{"6":{"11":true,"38":true,"51":true,"66":true,"80":true,"81":true,"103":true,"108":true,"242":true,"257":true,"307":true,"321":true,"342":true,"355":true,"384":true,"395":true,"414":true,"467":true,"480":true,"503":true,"608":true,"641":true,"642":true,"662":true,"828":true,"831":true,"933":true,"1028":true,"1061":true,"1272":true,"1552":true,"1727":true,"2191":true,"2253":true,"2450":true,"2468":true,"2516":true,"2594":true,"2708":true,"2937":true,"3042":true,"3058":true,"3490":true,"3778":true,"3857":true,"4526":true,"4748":true,"4941":true,"5296":true,"5385":true,"5678":true,"6359":true,"6531":true,"6609":true,"6638":true,"6723":true}},"cookies":{"6":true},"consent_type":1}; _ga_VBYSKTNF8V=GS1.1.1673514946.5.1.1673517613.0.0.0; _ga_K1R42ZM57S=GS1.1.1673514946.5.1.1673517613.0.0.0; _ga_XKJTHS007F=GS1.1.1673514946.5.1.1673517613.0.0.0; _tt_enable_cookie=1; _ttp=a7b0cda7-9087-405a-9895-3f63af64d54c; _mkto_trk=id:183-WCT-620&token:_mch-lenovo.com-1665230920111-34832; QuantumMetricUserID=74fbff938cad683a35a8b41e79875333; knexus_d13d58c021c52c7f020be3660bbea05b===QNxAjM3ETN3gzX452a; knexus_8a732e0ed93a959059be7e5cb2803679===QfiEDM4UjM5AzMyUjN2ETNxAjM3ETN3gzX452afRWazJiOi42bpN3clN3X0NXYsJCLiEDM4UjM5AzMyUjN2ETNxAjM3ETN3gzX452afRWazJiOi42bpN3clN3X05WZyJXdjJye; leid=1.huRjbCa2ec8; inside-us3=108873466-29014a8969c2e9106c9413f8b391b1ca49d05371015e34a2de5b7a4858008c78-0-0; _fbp=fb.1.1667666664753.798012961; IR_PI=3e0f36fb-5d29-11ed-8a73-a7ed7598257b%7C1673947216139; _rdt_uuid=1667666665904.7599b6e3-a726-4719-a1fb-473a30f64a40; _ga_1RPSEV71KD=GS1.1.1673858908.14.1.1673860840.35.0.0; _ga_X0H82YEL7G=GS1.1.1673858908.14.1.1673860840.35.0.0; _ga_LNFXZCR83J=GS1.1.1671094207.2.0.1671094214.0.0.0; _ga_S747NZ5XE2=GS1.1.1671094207.2.0.1671094214.0.0.0; _ga_740XK5GERP=GS1.1.1671094207.2.0.1671094215.0.0.0; inside-au=1180815480-383f2076c0fd5a57430a843fe082cd7db9a1c89e934dcf721fea43b4d43939f8-0-0; cto_bundle=xL911193dkRKeWwlMkZwSUtSSWIwNGF6elhDWkU5M2E2a1BKWHVqY3olMkJtZEZZbEY4OXZoMCUyQk9wZ1E3UmJDJTJGQ2tValhQbVdScEpGSlRXQ3p1bnVvVk5YJTJGbFBuMDQ2QkQ4am9TSEZaTEFIWFJOQ3lSSFhJZXpLdVZKdUlzTWhuMzdWeGU4eUh2N1NEMWlSVndFZ0FTYVJQWkJ4SFl3JTNEJTNE; mp_lenovo_au_mixpanel=%7B%22distinct_id%22%3A%20%2218448ade2a2371-022a22dd93a7038-c535426-144000-18448ade2a378d%22%2C%22bc_persist_updated%22%3A%201671040656780%7D; RT="z=1&dm=lenovo.com&si=576f3b94-7521-4819-a89a-aa9a1b124686&ss=lcykdddn&sl=7&tt=mes&bcn=%2F%2F684d0d4c.akstat.io%2F"; _gcl_au=1.1.698704869.1673517310; p3094257258_done=1; AKA_A2=A; ak_bmsc=C3B2CA1F63FB1E7A78BEE25416ADBFF2~000000000000000000000000000000~YAAQLG4/F5la5wSFAQAAk7zGuRJ7bGl+kGbDz0hX3bqTqBL0MNBOh2L8DfidEhjF1bKiRzGu+K797IygOqqQJY6RidbWsLbXCS7EGL5jq4tDYdU0MNMFc7jyVUfeFcGEnnMof9AG2O2ROxE5EvIUHJLNPYuS2PE70xwBU1hLvjp/yIFJZYl69k0VYdaFCio66tnWgsWbjEt3y4DPLYW14KA4Tv7JCBeU0DHHe/4DOqobgUhzgZYlw6seG9u3x1webrfSvQqpT4UCWM1zzpjAuyKjjNFAsNm8Puqrj4XyDQJQwLQPZxHTbnuTkBxEcOOh6WaNyjSqxpEHn+Ir8NWi1/oso+b6IHSWcJikhIs83EqdyA27qq8pNROcrHWv0PbnORg73StggPP573hhvJisUUDmLrB5bQDqcVFkGD7dsZsG47D47DsPBdFcGKY2MxX0qY/yw4gMraV4egvBpTNFoNJ8k78WhXfWp+EVqbTqiZbP+6M2N9yqmZDUjeGAAYAX+wzt6exG9NJQvAjHnLlrUBf21+ZeTTY2MJZlrtzZKOM09J3jccp03u/XOq5XmzS5tD64; bm_sz=C9EBE01986D4826F1B187AD9E26197E4~YAAQvAVaaDtcd6eFAQAASbDGuRLg053o2/EKkxtsX3/2G2qOyAT7kWMtA0dgyf0rICuyNEXRqcw203p3aBjcJ+DNtG5wZ4ZBkpHPEUHHr9FWoDcN6/Mq7WH3HqyaYQP8PfpPfusrWe5uWV7JFv6+HNvtW9caJXB2RAxw//yCzojcynJ7wgckpxEG9vlciX2NuHi8obCqLM+3F49MzFHmculQ5L3YnCu3aYvVlhmykl7Ljg9RiN77c+lk6qCY+31bycYK3iqXLtEY2ewCRVRdiv2J2qqnv4e5KgmXp49dBtwSSek=~4404532~3617840; bm_sv=1962EF9ACED2872EC3A0B41FF211A653~YAAQLG4/F2985wSFAQAATU3kuRL8opDOsXBEbIp66OjqTIZ6f+CpVMDTwWuEJCLXkwFRX3QHN8rkmq/iUteCueeNpKKG32pNRZIzVayc9Riih/tY3CrgurPcjs795T4t0KM8jxK12X5ToVfC5x4N9P9hM/6K0+EFpyAL9Q27HjFu9MakXD8Xsd+YSytdu6uO39HTgcXNb+f775pr37p5tvH5xZn14szcxoNHCmiRvHZVszse0tF2mqGndZaqnYrhE0I=~1; kndctr_F6171253512D2B8C0A490D45_AdobeOrg_cluster=ind1; bm_mi=313CED391B0E309705B3437EE1CC5655~YAAQvAVaaOFcd6eFAQAAbbjGuRKWLR8+tk/2yg0nJhufxxUNuLdW4Ce6iwSb8PvG6bVG4qzOunhxqdkQhb+LeP8/tdYm1Y35ffij1pOJH3RCr2vZQYmDKVTxbXOYksG2jdl2M3ZkA1mII1PZ6nw68jFiIjy10Zjwui5+q0dubk7BqOtETTflRDMT0S72VnjMOzM/TSQ9AgOmYDBuG4eUKR/KyDaZS0HxFvJHrN/ZK8wlfpjY/deTCC3vXciXP/roxPwvCxmFrfO/uCvK/UZEoa/909cK4v8Cm4dzVH86wndYd5UDRtiUKa0KVph8VFSod20VWF3YFAdEYwvwgApXGUwzgz2AcIPnpqJ953DRTXp30uRBuR39uAaERLmroBk=~1; s_inv=71930; s_ivc=true; s_dur=1673860812378; s_tot_rfd=0.56; s_eng_rfd=0.00; IR_gbd=lenovo.com; IR_3808=1673860816139%7C191037%7C1673860816139%7C%7C; QuantumMetricSessionID=525bf46a8c64d28f8f2907c3e6ded9a8; BVBRANDSID=c1740e8a-c7d0-43ed-8930-46fcab3b6e77; _uetsid=c8e91cc0942611edb3ae1fbf4b5ae05b; _uetvid=1b3218305d2911ed9e5359d95ef42fa7; mp_lenovo_us_mixpanel=%7B%22distinct_id%22%3A%20%2218448ade2a2371-022a22dd93a7038-c535426-144000-18448ade2a378d%22%2C%22bc_persist_updated%22%3A%201673517311044%7D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'productNumber': 'LEN101T0017',
}


def info():
    a=row['ID']
    params['productNumber'] = a
    headers['Referer'] = row['URL']
    # response = c.get('https://openapi.lenovo.com/us/en/online/product/getTechSpecs',params= {'render_js':False,'wait':5000,'premium_proxy':True,'country_code':'us',"block_resources":False})
    response = requests.get(
    'https://openapi.lenovo.com/us/en/online/product/getTechSpecs',
    params=params,
    # cookies=cookies,
    headers=headers,
    )
    print(response,response.url)
    Graphics = ''
    Display = ''
    Processor = ''
    Memory = ''
    Storage = ''
    js = response.json()
    # print(js)
    allinfo = js['data']['tables'][0]['specs']
    for i in allinfo:
        textt = i['headline']
        if textt == 'Graphics':
            Graphics = bs(i['text']).text
        if textt == 'Processor':
            Processor = bs(i['text']).text
        if textt == 'Memory':
            Memory = bs(i['text']).text
        if textt == 'Storage':
            Storage = bs(i['text']).text
        if textt == 'Display':
            Display = bs(i['text']).text
        data = {
            'Processor':Processor,
            'Graphics':Graphics,
            'Display':Display,
            'Memory':Memory,
            'Storage':Storage

        }
        return data

alldata = []
def detailpage(url):
    url = row['URL']
    time.sleep(3)
    # r = c.get(url,params= {'render_js':False,'wait':5000,'premium_proxy':True,'country_code':'us',"block_resources":False})
    r = s.get(url)
    tree=html.fromstring(r.text) 
    soup = bs(r.text,'html.parser')
    print(r,url)
    try:
        name = soup.find('h2','product_summary').text
    except:
        name = ""
    try:
        space = soup.find('div','banner_content_desc').find('ul').text
    except:
        space = ""
    try:
        image = '||'.join(['https:'+i.find('img').get('src') for i in soup.find_all('div','image-pic')])
    except:
        image = ""
    try:
        Bread = '>'.join([i.find('a').text for i in soup.find_all('li','breadcrumb_item')])
    except:
        Bread = ""
    # Processor = ''.join(tree.xpath('//meta[@name="Processor"]/@content'))
    # memory = ''.join(tree.xpath('//meta[@name="memory"]/@content'))
    # hard_drive = ''.join(tree.xpath('//meta[@name="hard_drive"]/@content'))
    # display_type = ''.join(tree.xpath('//meta[@name="display_type"]/@content'))
    try:
        stock = soup.find('div',{'data-tkey':'in.stock'}).text
    except:
        stock = ""
    if re.search('"price":(.*?)},',r.text).group(1):
        price = re.search('"price":(.*?)},',r.text).group(1)
    elif soup.find('meta',{'name':'productpromotionprice'}):
        price = soup.find('meta',{'name':'productpromotionprice'}).get('content')
    else:
        price = ""
    Specification = info()
    data = {
        'landinUrl':url,
        'name':name,
        'space':space,
        'image':image,
        'Bread':Bread,
        'stock':stock,
        'price':price, 
    }
    data.update(Specification)
    xl.writerow(data.values())
    alldata.append(data)
    print(data)


df = pd.read_excel('lenovo_us.xlsx',sheet_name='Sheet3')
with concurrent.futures.ThreadPoolExecutor(max_workers = 10) as executor :
    for l in  range(39,len(df)):
        row = df.iloc[l].to_dict()
        detailpage(row)

    


df = pd.DataFrame(alldata)
df.to_excel('lenovofinal.xlsx', index=False)
