import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import Session
s=Session()
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
url = 'https://kyliecosmetics.com/en-us/kylie-cosmetics/shop-all'

xl = csv.writer(open('kylie.csv','w',newline=""))
xl.writerow(['Id','List_Name','API_link','pro_Url','List_Price','List_image','Brand',
    'Name','longDescription','subTitle','shortDiscription','SKU','Usage','keys_feature','Pro_Details'])

# xl=csv.writer(open('Disesas.csv','w',newline=''))
# xl.writerow(['Name','Dease_URL','Dease_image'])

cookies = {
    'OptanonConsent': 'isIABGlobal=false&datestamp=Sun+Dec+18+2022+13%3A00%3A54+GMT%2B0530+(India+Standard+Time)&version=202208.1.0&hosts=&consentId=25bdbdc3-5a33-4308-bb9a-c05f5214d5b2&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=IN%3BDL&AwaitingReconsent=false',
    'REGION': 'EU',
    'forterToken': '896e5a1f3dd84df2be7d2488e04b9dcd_1671348417381__UDF43-mnf-anf_13ck',
    'AMCV_157D1990530FC26A0A490D4C%40AdobeOrg': '-1124106680%7CMCIDTS%7C19345%7CMCMID%7C37239298572878256952823852413478574357%7CMCAAMLH-1671952518%7C12%7CMCAAMB-1671952518%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1671354918s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19350%7CvVersion%7C5.2.0',
    'mbox': 'PC#9accf94a4a7146408996042657bfca0f.31_0#1734418734|session#ac5800a0a37e4388ab8f2a2ae83d9070#1671349579',
    'NoCookie': 'true',
    '_attn_': 'eyJ1Ijoie1wiY29cIjoxNjcxMTczOTMyMjkxLFwidW9cIjoxNjcxMTczOTMyMjkxLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjdlOWViNjAzN2EyNDQ2YzdhY2Q5NzRmNWYxMjZmZGJiXCJ9In0=',
    'tpc_a': 'e639e610217247fd8dca2d9846e3fccf.1671173932.0dN.1671347721',
    '__attentive_id': '7e9eb6037a2446c7acd974f5f126fdbb',
    '__attentive_cco': '1671173932292',
    's_visnum': '1671348651858',
    's_nr': '1671348651859-Repeat',
    'adobeujs-optin': '%7B%22aam%22%3Atrue%2C%22adcloud%22%3Atrue%2C%22aa%22%3Atrue%2C%22campaign%22%3Afalse%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Afalse%2C%22target%22%3Afalse%2C%22mediaaa%22%3Afalse%7D',
    '_gcl_au': '1.1.20662865.1671173936',
    '_ga': 'GA1.1.1358638521.1671173937',
    '_gid': 'GA1.2.198980796.1671173937',
    '_fbp': 'fb.1.1671173937240.1989599101',
    'OptanonAlertBoxClosed': '2022-12-16T06:58:59.572Z',
    'QuantumMetricUserID': 'd61432f2c046f3de4c2ddeb3cebc8449',
    '_ga_HJXEVNV20J': 'GS1.1.1671347716.8.1.1671348654.0.0.0',
    'affinity': '"58f6dc57388db29d"',
    'vuex-en-eu': '{%22product%22:{%22variantId%22:null}%2C%22user%22:{%22isModalOpen%22:false%2C%22customerProfile%22:{}}%2C%22notify%22:{%22isSiteEnabled%22:true%2C%22isFormCompleted%22:false%2C%22isNotifyModalOpen%22:false%2C%22user%22:{}%2C%22products%22:[]%2C%22pendingProduct%22:%22%22%2C%22buttonLabel%22:%22NOTIFY%20ME%22%2C%22successLabel%22:%22Notification%20successful!%22%2C%22currentProductName%22:%22%22%2C%22serviceData%22:{%22endpointUrl%22:%22p28q8w4y93.execute-api.eu-central-1.amazonaws.com/prod%22%2C%22apiKey%22:%220pZ2yOLMkgvy7iw87lCyBzgvbOKN1FKuzVsIS6q0%22}}}',
    'at_check': 'true',
    'AMCVS_157D1990530FC26A0A490D4C%40AdobeOrg': '1',
    's_ppvl': 'EU%253Akylie-cosmetics%253Ashop-all%253Anew%2C97%2C97%2C14770%2C1536%2C704%2C1536%2C864%2C1.25%2CP',
    's_ppv': 'EU%253Akylie-cosmetics%253Ashop-all%2C33%2C31%2C14964%2C1536%2C381%2C1536%2C864%2C1.25%2CP',
    's_cc': 'true',
    's_sq': '%5B%5BB%5D%5D',
    'BVImplmain_site': '16784',
    'QuantumMetricSessionID': '23d6ebbd357031b979194e0483fd97f3',
    'gpv_e7': 'EU%3Akylie-cosmetics%3Ashop-all',
    's_visnum_s': 'Less%20than%201%20day',
    's_visit': '1',
    '__attentive_pv': '2',
    '__attentive_ss_referrer': 'ORGANIC',
    '__attentive_dv': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://kyliecosmetics.com/en-eu/kylie-cosmetics/shop-all',
    # 'Cookie': 'OptanonConsent=isIABGlobal=false&datestamp=Sun+Dec+18+2022+13%3A00%3A54+GMT%2B0530+(India+Standard+Time)&version=202208.1.0&hosts=&consentId=25bdbdc3-5a33-4308-bb9a-c05f5214d5b2&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=IN%3BDL&AwaitingReconsent=false; REGION=EU; forterToken=896e5a1f3dd84df2be7d2488e04b9dcd_1671348417381__UDF43-mnf-anf_13ck; AMCV_157D1990530FC26A0A490D4C%40AdobeOrg=-1124106680%7CMCIDTS%7C19345%7CMCMID%7C37239298572878256952823852413478574357%7CMCAAMLH-1671952518%7C12%7CMCAAMB-1671952518%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1671354918s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19350%7CvVersion%7C5.2.0; mbox=PC#9accf94a4a7146408996042657bfca0f.31_0#1734418734|session#ac5800a0a37e4388ab8f2a2ae83d9070#1671349579; NoCookie=true; _attn_=eyJ1Ijoie1wiY29cIjoxNjcxMTczOTMyMjkxLFwidW9cIjoxNjcxMTczOTMyMjkxLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjdlOWViNjAzN2EyNDQ2YzdhY2Q5NzRmNWYxMjZmZGJiXCJ9In0=; tpc_a=e639e610217247fd8dca2d9846e3fccf.1671173932.0dN.1671347721; __attentive_id=7e9eb6037a2446c7acd974f5f126fdbb; __attentive_cco=1671173932292; s_visnum=1671348651858; s_nr=1671348651859-Repeat; adobeujs-optin=%7B%22aam%22%3Atrue%2C%22adcloud%22%3Atrue%2C%22aa%22%3Atrue%2C%22campaign%22%3Afalse%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Afalse%2C%22target%22%3Afalse%2C%22mediaaa%22%3Afalse%7D; _gcl_au=1.1.20662865.1671173936; _ga=GA1.1.1358638521.1671173937; _gid=GA1.2.198980796.1671173937; _fbp=fb.1.1671173937240.1989599101; OptanonAlertBoxClosed=2022-12-16T06:58:59.572Z; QuantumMetricUserID=d61432f2c046f3de4c2ddeb3cebc8449; _ga_HJXEVNV20J=GS1.1.1671347716.8.1.1671348654.0.0.0; affinity="58f6dc57388db29d"; vuex-en-eu={%22product%22:{%22variantId%22:null}%2C%22user%22:{%22isModalOpen%22:false%2C%22customerProfile%22:{}}%2C%22notify%22:{%22isSiteEnabled%22:true%2C%22isFormCompleted%22:false%2C%22isNotifyModalOpen%22:false%2C%22user%22:{}%2C%22products%22:[]%2C%22pendingProduct%22:%22%22%2C%22buttonLabel%22:%22NOTIFY%20ME%22%2C%22successLabel%22:%22Notification%20successful!%22%2C%22currentProductName%22:%22%22%2C%22serviceData%22:{%22endpointUrl%22:%22p28q8w4y93.execute-api.eu-central-1.amazonaws.com/prod%22%2C%22apiKey%22:%220pZ2yOLMkgvy7iw87lCyBzgvbOKN1FKuzVsIS6q0%22}}}; at_check=true; AMCVS_157D1990530FC26A0A490D4C%40AdobeOrg=1; s_ppvl=EU%253Akylie-cosmetics%253Ashop-all%253Anew%2C97%2C97%2C14770%2C1536%2C704%2C1536%2C864%2C1.25%2CP; s_ppv=EU%253Akylie-cosmetics%253Ashop-all%2C33%2C31%2C14964%2C1536%2C381%2C1536%2C864%2C1.25%2CP; s_cc=true; s_sq=%5B%5BB%5D%5D; BVImplmain_site=16784; QuantumMetricSessionID=23d6ebbd357031b979194e0483fd97f3; gpv_e7=EU%3Akylie-cosmetics%3Ashop-all; s_visnum_s=Less%20than%201%20day; s_visit=1; __attentive_pv=2; __attentive_ss_referrer=ORGANIC; __attentive_dv=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

def detailpage(url):
    r = s.get(url)
    pro_detail = r.json()
    # print(r.json())
    Name = pro_detail['self']['name']
    longDescription = bs("".join(pro_detail['self']['longDescription']),'html.parser').text
    subTitle = pro_detail['self']['productHandle']
    shortDiscriptions = pro_detail['self'].get('shortDescription')
    SKU = pro_detail['self'].get('sku')
    try:
        Usage = bs(''.join(pro_detail['self']['productDetails']['accordion']['usage'].get('usageTips'))).text
    except:
        Usage ='no'
    Keys_feature = bs("".join(pro_detail['self']['productDetails']['accordion']['features']['features'][0]['features'])).text
    Pro_Details = pro_detail['self']['productDetails']['accordion']['details']['detailsPdp']
    

    data = {

        'Name':Name,
        'longDescription':longDescription,#
        'subTitle':subTitle,
        'shortDiscription':shortDiscriptions,
        'SKU':SKU,
        'Usage':Usage,#
        'keys_feature':Keys_feature,#
        'Pro_Details':Pro_Details#
    }
    return data



alldata = []
def listpage():
    # url =

    response = requests.get(
        'https://kyliecosmetics.com/content/kylie-beauty/countries/eu/en/kylie-cosmetics/shop-all/jcr:content/root/main_area/product_list_copy.list.json/0.json',
        cookies=cookies,
        headers=headers,
    )
    js = response.json()
    products = js
    for product in products:
        Id = product.get('right').get('code')
        Name = product.get('right').get('name')
        pro_Url = 'https://kyliecosmetics.com'+product.get('right').get('url')
        API_link = pro_Url.split('#')[0]+'/jcr:content.variantdata.json'
        Price = product.get('right').get('price')
        List_image = product.get('right').get('imageSrc')
        Brand = product.get('right').get('brand')
        detail = detailpage(API_link)
        # print(pro_Url)
        datas = { 
            'landingUrl':url,
            'Id':Id,
            'List_Name':Name,
            'API_link':API_link,
            'pro_Url': pro_Url,
            'List_Price':Price,
            'List_image':List_image,
            'Brand':Brand,
        }  

        xl.writerow(datas.values()) 
        datas.update(detail)
        alldata.append(datas)
        print(datas)

listpage()
df = pd.DataFrame(alldata)
df.to_excel('Kyliecosmetics.xlsx',index=False)

