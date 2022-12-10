import re
import json
import requests
import pandas as pd
from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html
s = Session()
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
# with open('file.json','w') as file:
    # file.write(json.dumps(data,indent=4))



cookies = {
    'wdi': '1|481E2A5B914FD6DA|0x1.8e3b5dd1d3c3ap+30|ced26f0929f06bb8',
    'location': '%7B%22max_latitude%22%3A+37.81602226140252%2C+%22country%22%3A+%22US%22%2C+%22latitude%22%3A+37.775123257209394%2C+%22county%22%3A+%22San+Francisco+County%22%2C+%22display%22%3A+%22San+Francisco%2C+CA%22%2C+%22zip%22%3A+%22%22%2C+%22parent_id%22%3A+371%2C+%22city%22%3A+%22San+Francisco%22%2C+%22state%22%3A+%22CA%22%2C+%22location_type%22%3A+%22locality%22%2C+%22provenance%22%3A+%22YELP_GEOCODING_ENGINE%22%2C+%22min_longitude%22%3A+-122.51781463623047%2C+%22place_id%22%3A+%221237%22%2C+%22min_latitude%22%3A+37.706368356809776%2C+%22unformatted%22%3A+%22San+Francisco%2C+CA%22%2C+%22accuracy%22%3A+4%2C+%22address2%22%3A+%22%22%2C+%22address1%22%3A+%22%22%2C+%22max_longitude%22%3A+-122.3550796508789%2C+%22longitude%22%3A+-122.41931994395134%2C+%22address3%22%3A+%22%22%2C+%22borough%22%3A+%22%22%2C+%22isGoogleHood%22%3A+false%2C+%22language%22%3A+null%2C+%22neighborhood%22%3A+%22%22%2C+%22polygons%22%3A+null%2C+%22usingDefaultZip%22%3A+false%2C+%22confident%22%3A+null%7D',
    'hl': 'en_US',
    'xcj': '1|krrTklHY-yX-eTez4SwmayUnJCjnwcR2u5y0k5jpVXY',
    'ppn': '%7B%22impressions%22%3A+44%2C+%22dismissed%22%3A+false%7D',
    '_ga': 'GA1.2.481E2A5B914FD6DA',
    '_gid': 'GA1.2.785424698.1670305545',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Dec+07+2022+10%3A59%3A48+GMT%2B0530+(India+Standard+Time)&version=6.34.0&isIABGlobal=false&hosts=&consentId=22eb0420-423a-43a9-a94d-321748d593c4&interactionCount=1&landingPath=NotLandingPage&groups=BG51%3A1%2CC0003%3A1%2CC0002%3A1%2CC0001%3A1%2CC0004%3A1&AwaitingReconsent=false',
    'g_state': '{"i_p":1670402271251,"i_l":2}',
    '_gcl_au': '1.1.237331699.1670305573',
    '_scid': 'c7550fcb-5f44-40f8-8f9e-68239da5d9ff',
    '_sctr': '1|1670265000000',
    'qntcst': 'D',
    '_tt_enable_cookie': '1',
    '_ttp': 'c95fb042-7fef-4d8b-a964-c1abdca5ddbe',
    '__qca': 'P0-2108149038-1670305575338',
    '__adroll_fpc': 'f9284221ce801eb9e78327d49d3d85f6-1670305578081',
    '__ar_v4': 'BHPKS4B4ONEJJMGH4QCJZR%3A20230005%3A61%7CQB5JPFIKRZDSBOZSULG4YB%3A20230005%3A61%7C7YX6SJQ4RZAMPB6LZ7CHFF%3A20230005%3A61',
    '_fbp': 'fb.1.1670305579235.1441112980',
    'G_ENABLED_IDPS': 'google',
    'bse': 'd9b9ce805e9547c7a30632dc0702ce36',
    'recentlocations': '',
    'rsp': '%7B%22date%22%3A%222022-12-07%22%2C%22time%22%3A%221900%22%2C%22partySize%22%3A2%7D',
    'adc': 'EOM6CItD6sI5P3a-JV61_Q%3Af6pY59LAxe9D8aFh1Bf1Pg%3A1670391097',
    '_uetsid': '4bc58d60752911ed905219f2c13bbbd9',
    '_uetvid': '4bc59c60752911edb7fdd34f4edd6b4b',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.yelp.com/search?cflt=burgers&find_loc=San+Francisco%2C+CA&start=10',
    'Connection': 'keep-alive',
    # 'Cookie': 'wdi=1|481E2A5B914FD6DA|0x1.8e3b5dd1d3c3ap+30|ced26f0929f06bb8; location=%7B%22max_latitude%22%3A+37.81602226140252%2C+%22country%22%3A+%22US%22%2C+%22latitude%22%3A+37.775123257209394%2C+%22county%22%3A+%22San+Francisco+County%22%2C+%22display%22%3A+%22San+Francisco%2C+CA%22%2C+%22zip%22%3A+%22%22%2C+%22parent_id%22%3A+371%2C+%22city%22%3A+%22San+Francisco%22%2C+%22state%22%3A+%22CA%22%2C+%22location_type%22%3A+%22locality%22%2C+%22provenance%22%3A+%22YELP_GEOCODING_ENGINE%22%2C+%22min_longitude%22%3A+-122.51781463623047%2C+%22place_id%22%3A+%221237%22%2C+%22min_latitude%22%3A+37.706368356809776%2C+%22unformatted%22%3A+%22San+Francisco%2C+CA%22%2C+%22accuracy%22%3A+4%2C+%22address2%22%3A+%22%22%2C+%22address1%22%3A+%22%22%2C+%22max_longitude%22%3A+-122.3550796508789%2C+%22longitude%22%3A+-122.41931994395134%2C+%22address3%22%3A+%22%22%2C+%22borough%22%3A+%22%22%2C+%22isGoogleHood%22%3A+false%2C+%22language%22%3A+null%2C+%22neighborhood%22%3A+%22%22%2C+%22polygons%22%3A+null%2C+%22usingDefaultZip%22%3A+false%2C+%22confident%22%3A+null%7D; hl=en_US; xcj=1|krrTklHY-yX-eTez4SwmayUnJCjnwcR2u5y0k5jpVXY; ppn=%7B%22impressions%22%3A+44%2C+%22dismissed%22%3A+false%7D; _ga=GA1.2.481E2A5B914FD6DA; _gid=GA1.2.785424698.1670305545; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Dec+07+2022+10%3A59%3A48+GMT%2B0530+(India+Standard+Time)&version=6.34.0&isIABGlobal=false&hosts=&consentId=22eb0420-423a-43a9-a94d-321748d593c4&interactionCount=1&landingPath=NotLandingPage&groups=BG51%3A1%2CC0003%3A1%2CC0002%3A1%2CC0001%3A1%2CC0004%3A1&AwaitingReconsent=false; g_state={"i_p":1670402271251,"i_l":2}; _gcl_au=1.1.237331699.1670305573; _scid=c7550fcb-5f44-40f8-8f9e-68239da5d9ff; _sctr=1|1670265000000; qntcst=D; _tt_enable_cookie=1; _ttp=c95fb042-7fef-4d8b-a964-c1abdca5ddbe; __qca=P0-2108149038-1670305575338; __adroll_fpc=f9284221ce801eb9e78327d49d3d85f6-1670305578081; __ar_v4=BHPKS4B4ONEJJMGH4QCJZR%3A20230005%3A61%7CQB5JPFIKRZDSBOZSULG4YB%3A20230005%3A61%7C7YX6SJQ4RZAMPB6LZ7CHFF%3A20230005%3A61; _fbp=fb.1.1670305579235.1441112980; G_ENABLED_IDPS=google; bse=d9b9ce805e9547c7a30632dc0702ce36; recentlocations=; rsp=%7B%22date%22%3A%222022-12-07%22%2C%22time%22%3A%221900%22%2C%22partySize%22%3A2%7D; adc=EOM6CItD6sI5P3a-JV61_Q%3Af6pY59LAxe9D8aFh1Bf1Pg%3A1670391097; _uetsid=4bc58d60752911ed905219f2c13bbbd9; _uetvid=4bc59c60752911edb7fdd34f4edd6b4b',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'cflt': 'burgers',
    'find_loc': 'San Francisco, CA',
    'parent_request_id': '84e014ec2e10bf19',
    'request_origin': 'user',
}


def detailpage(url):
    r = s.get(url)
    soup = bs(r.text, 'html.parsser')
    Title = soup.find('h1').text
    review = soup.find('a','css-1m051bw').text
    address = soup.find('p','css-qyp8bo').text
    websiteUrl = soup.findAll('a','css-1um3nx')[4].get('href')
    direction = soup.findAll('a','css-1um3nx')[6].get('href')

    return {
        'Title': Title,
        'review': review,
        'address': address,
        'websiteUrl': websiteUrl,
        'direction': direction
    }





alldata = []
def listpage(url):
    # nextpage = url

    # while nextpage:
    for i in range(0,230,10):
        url = 'https://www.yelp.com/search?cflt=burgers&find_loc=San+Francisco%2C+CA&start=0'
        params['start'] = str(i)
        response = requests.get('https://www.yelp.com/search/snippet', params=params, cookies=cookies, headers=headers)
        js = response.json()
        links = js['searchPageProps']['mainContentComponentsListProps']
        for l in links:
            if l['searchResultLayoutType'] == 'iaResult' and l['searchResultBusiness']['ranking']!=None:
                pro_link = 'https://www.yelp.com'+l.get('searchResultBusiness').get('businessUrl')
                detail = detailpage(pro_link)
                data = {'pro_link':pro_link}
                data.update(detail)
                alldata.append(data)
        # print(js)
        # if soup.find('a','next-link navigation-button__09f24__m9qRz css-144i0wq'):
        #     nextpage = soup.find('a','next-link navigation-button__09f24__m9qRz css-144i0wq').get('href')
        #     print(f'THIS IS NEXT PAGE.. {nextpage}................................')
        # else:
        #     nextpage = False


listpage(url)
df = pd.DataFrame(alldata)
df.to_excel('yelp.xlsx',index=False)
print(alldata)