import requests 
from requests import Session
s = Session()
# s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
# url = 'https://www.vijaysales.com/home-appliances/air-conditioners'
# api = 'https://www.vijaysales.com/Handlers/getProductData.ashx?q=SearchPageProducts_1_home-appliances_air-conditioners&catid=6&cityid=1&fvids=480,#,&fid=0&Index=11&sortBy=&minPrice=25989&maxPrice=138000&actul=480,#,&BucketID=0&isND=1&isAcc=False&BrandID='
# r = s.get(api)
cookies = {
    'AWSALB': '2C9UTc1B+1DW1U4vcoMhtItWE09JLfR9K4Bs/6JgybTfUquaD/gadf4VApweXYoK7pn9xmrMsSyu+VmGUVUZFAhTHN04iHjTeL+GTEHmtse1hW5wtZej9//AhtDQ',
    'AWSALBCORS': '2C9UTc1B+1DW1U4vcoMhtItWE09JLfR9K4Bs/6JgybTfUquaD/gadf4VApweXYoK7pn9xmrMsSyu+VmGUVUZFAhTHN04iHjTeL+GTEHmtse1hW5wtZej9//AhtDQ',
    '_gcl_aw': 'GCL.1680347514.CjwKCAjwrJ-hBhB7EiwAuyBVXZryG8Xd3DRDHJEjWpWXK7p_xhkpc9abKAQldwG8qw_f6Yi3YJFugxoC2lYQAvD_BwE',
    '_gcl_au': '1.1.1443720213.1680347514',
    'unbxd.userId': 'uid-1680347514324-84114',
    'mfKey': '176l6f1.1680347514397',
    'mf_visitid': '18hhv04.1680347514397',
    'mf_utms': '%7B%22utm_source%22%3A%22google_search%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22pt-google-vijaysales-na-gs-purchase-brand-na-in-all-24-Oct-2020%22%2C%22utm_term%22%3A%22vijay%2520sales%22%2C%22utm_content%22%3A%22529936422896%22%2C%22adgroup%22%3A%22112819201595%22%2C%22matchtype%22%3A%22e%22%2C%22devicemodel%22%3A%22%22%2C%22device%22%3A%22c%22%2C%22network%22%3A%22g%22%2C%22placement%22%3A%22%22%2C%22gclid%22%3A%22CjwKCAjwrJ-hBhB7EiwAuyBVXZryG8Xd3DRDHJEjWpWXK7p_xhkpc9abKAQldwG8qw_f6Yi3YJFugxoC2lYQAvD_BwE%22%7D',
    '_nv_uid': '38961852.1680347516.67172ed1-e60c-405a-a4ba-2983708ed272.1680616926.1680673801.6.0',
    '_nv_utm': '38961852.1680347516.6.1.dXRtc3JjPWdvb2dsZXx1dG1jY249cHQtZ29vZ2xlLXZpamF5c2FsZXMtbmEtZ3MtcHVyY2hhc2UtYnJhbmQtbmEtaW4tYWxsLTI0LU9jdC0yMDIwfHV0bWNtZD1jcGN8dXRtY3RyPXZpamF5K3NhbGVzfHV0bWNjdD01Mjk5MzY0MjI4OTZ8Z2NsaWQ9Q2p3S0NBandySi1oQmhCN0Vpd0F1eUJWWFpyeUc4WGQzRFJESEpFaldwV1hLN3BfeGhrcGM5YWJLQVFsZHdHOHF3X2Y2WWkzWUpGdWd4b0MybFlRQXZEX0J3RQ==',
    '_nv_did': '38961852.1680347516.2409:4050:d98:c2e5:2d2b:22d9:940c:95aewd15k',
    '_nv_hit': '38961852.1680673801.cHZpZXc9MQ==',
    '_ga': 'GA1.2.741139552.1680347515',
    '_gac_UA-26907894-4': '1.1680347515.CjwKCAjwrJ-hBhB7EiwAuyBVXZryG8Xd3DRDHJEjWpWXK7p_xhkpc9abKAQldwG8qw_f6Yi3YJFugxoC2lYQAvD_BwE',
    '_gac_UA-26907894-5': '1.1680347518.CjwKCAjwrJ-hBhB7EiwAuyBVXZryG8Xd3DRDHJEjWpWXK7p_xhkpc9abKAQldwG8qw_f6Yi3YJFugxoC2lYQAvD_BwE',
    '_clck': '15ne5j3|1|fai|0',
    '_fbp': 'fb.1.1680347516239.378660695',
    '_nv_push_times': '1',
    '_gid': 'GA1.2.675340249.1680589185',
    'ASP.NET_SessionId': 'ly2pofj4farejxmlfdprmys2',
    '__AntiXsrfToken': '7498c7bf6a1e4b1b97d46c42e2511780',
    'Mypreurl': '',
    'mycity': 'cityId=1&city=Mumbai&IsPreOrder=false&isDefault=true',
    'UPinT': 'pin=400001',
    'UPinCode': 'pinC=400001',
    'mycityclose': 'true',
    '_nv_sess': '38961852.1680673801.NWMA7HseIIreap3t5bqTbu1DFe9b3dHspnhgF5eJ2rZLWoWMVh',
    'unbxd.visit': 'repeat',
    'unbxd.visitId': 'visitId-1680673802609-26329',
    '_gat_UA-26907894-4': '1',
    '_gat_UA-26907894-5': '1',
    '_uetsid': 'b1af9c50d2b011eda5e1c7d51e434b08',
    '_uetvid': '02bbac50d07e11ed9251673bc01fe8f8',
    '_dc_gtm_UA-26907894-5': '1',
    '_clsk': 'h2i4wg|1680673804805|1|1|o.clarity.ms/collect',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json; charset=utf-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www.vijaysales.com/home-appliances/air-conditioners',
    # 'Cookie': 'AWSALB=2C9UTc1B+1DW1U4vcoMhtItWE09JLfR9K4Bs/6JgybTfUquaD/gadf4VApweXYoK7pn9xmrMsSyu+VmGUVUZFAhTHN04iHjTeL+GTEHmtse1hW5wtZej9//AhtDQ; AWSALBCORS=2C9UTc1B+1DW1U4vcoMhtItWE09JLfR9K4Bs/6JgybTfUquaD/gadf4VApweXYoK7pn9xmrMsSyu+VmGUVUZFAhTHN04iHjTeL+GTEHmtse1hW5wtZej9//AhtDQ; _gcl_aw=GCL.1680347514.CjwKCAjwrJ-hBhB7EiwAuyBVXZryG8Xd3DRDHJEjWpWXK7p_xhkpc9abKAQldwG8qw_f6Yi3YJFugxoC2lYQAvD_BwE; _gcl_au=1.1.1443720213.1680347514; unbxd.userId=uid-1680347514324-84114; mfKey=176l6f1.1680347514397; mf_visitid=18hhv04.1680347514397; mf_utms=%7B%22utm_source%22%3A%22google_search%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22pt-google-vijaysales-na-gs-purchase-brand-na-in-all-24-Oct-2020%22%2C%22utm_term%22%3A%22vijay%2520sales%22%2C%22utm_content%22%3A%22529936422896%22%2C%22adgroup%22%3A%22112819201595%22%2C%22matchtype%22%3A%22e%22%2C%22devicemodel%22%3A%22%22%2C%22device%22%3A%22c%22%2C%22network%22%3A%22g%22%2C%22placement%22%3A%22%22%2C%22gclid%22%3A%22CjwKCAjwrJ-hBhB7EiwAuyBVXZryG8Xd3DRDHJEjWpWXK7p_xhkpc9abKAQldwG8qw_f6Yi3YJFugxoC2lYQAvD_BwE%22%7D; _nv_uid=38961852.1680347516.67172ed1-e60c-405a-a4ba-2983708ed272.1680616926.1680673801.6.0; _nv_utm=38961852.1680347516.6.1.dXRtc3JjPWdvb2dsZXx1dG1jY249cHQtZ29vZ2xlLXZpamF5c2FsZXMtbmEtZ3MtcHVyY2hhc2UtYnJhbmQtbmEtaW4tYWxsLTI0LU9jdC0yMDIwfHV0bWNtZD1jcGN8dXRtY3RyPXZpamF5K3NhbGVzfHV0bWNjdD01Mjk5MzY0MjI4OTZ8Z2NsaWQ9Q2p3S0NBandySi1oQmhCN0Vpd0F1eUJWWFpyeUc4WGQzRFJESEpFaldwV1hLN3BfeGhrcGM5YWJLQVFsZHdHOHF3X2Y2WWkzWUpGdWd4b0MybFlRQXZEX0J3RQ==; _nv_did=38961852.1680347516.2409:4050:d98:c2e5:2d2b:22d9:940c:95aewd15k; _nv_hit=38961852.1680673801.cHZpZXc9MQ==; _ga=GA1.2.741139552.1680347515; _gac_UA-26907894-4=1.1680347515.CjwKCAjwrJ-hBhB7EiwAuyBVXZryG8Xd3DRDHJEjWpWXK7p_xhkpc9abKAQldwG8qw_f6Yi3YJFugxoC2lYQAvD_BwE; _gac_UA-26907894-5=1.1680347518.CjwKCAjwrJ-hBhB7EiwAuyBVXZryG8Xd3DRDHJEjWpWXK7p_xhkpc9abKAQldwG8qw_f6Yi3YJFugxoC2lYQAvD_BwE; _clck=15ne5j3|1|fai|0; _fbp=fb.1.1680347516239.378660695; _nv_push_times=1; _gid=GA1.2.675340249.1680589185; ASP.NET_SessionId=ly2pofj4farejxmlfdprmys2; __AntiXsrfToken=7498c7bf6a1e4b1b97d46c42e2511780; Mypreurl=; mycity=cityId=1&city=Mumbai&IsPreOrder=false&isDefault=true; UPinT=pin=400001; UPinCode=pinC=400001; mycityclose=true; _nv_sess=38961852.1680673801.NWMA7HseIIreap3t5bqTbu1DFe9b3dHspnhgF5eJ2rZLWoWMVh; unbxd.visit=repeat; unbxd.visitId=visitId-1680673802609-26329; _gat_UA-26907894-4=1; _gat_UA-26907894-5=1; _uetsid=b1af9c50d2b011eda5e1c7d51e434b08; _uetvid=02bbac50d07e11ed9251673bc01fe8f8; _dc_gtm_UA-26907894-5=1; _clsk=h2i4wg|1680673804805|1|1|o.clarity.ms/collect',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'q': 'SearchPageProducts_1_home-appliances_air-conditioners',
    'catid': '6',
    'cityid': '1',
    'fvids': '480,#,',
    'fid': '0',
    'Index': '2',
    'sortBy': '',
    'minPrice': '25989',
    'maxPrice': '138000',
    'actul': '480,#,',
    'BucketID': '0',
    'isND': '1',
    'isAcc': 'False',
    'BrandID': '',
}

page = 1
# while True:
for i in range(1, 5):
    params['Index'] = page
    response = requests.get(
        'https://www.vijaysales.com/Handlers/getProductData.ashx',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    # print(response.json())
    js = response.json()
    products = js['SearchData']
    for i in products:
        PID = i.get('PID')
        pro_url = i.get('URLName')
        DName = i.get('DName')
        MRPrice = i.get('MRPrice')
        image = i.get('Pimage')
        print(response.url,'..............................................')
        print(PID,pro_url,DName, MRPrice,image)
        # print(products.keys())
    page += 1
