import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from requests import Session
s=Session()
cookies = {
    'viewNumR1': '100',
    'isPopupEnabledR1': 'true',
    'pocketViewR1': 'front',
    'sourcetracking': 'google',
    'sourcetrackingdate': '1666850517250',
    'currency': 'USD',
    'currencyOverride': 'INR',
    'userLanguagePref': 'en',
    'fontsLoaded': '1',
    'altexp': '%7B%22896%22%3A0%2C%221283%22%3A1%2C%221412%22%3A1%2C%221157%22%3A1%2C%221031%22%3A1%2C%221543%22%3A0%2C%221546%22%3A1%2C%221549%22%3A0%2C%221552%22%3A0%2C%221424%22%3A1%2C%221298%22%3A0%2C%221555%22%3A0%2C%221558%22%3A0%2C%221430%22%3A0%2C%221304%22%3A0%2C%221561%22%3A0%2C%221433%22%3A0%2C%221179%22%3A1%2C%221436%22%3A0%2C%221567%22%3A1%2C%221439%22%3A0%2C%221570%22%3A1%2C%221442%22%3A1%2C%221573%22%3A1%2C%22677%22%3A1%2C%221445%22%3A1%2C%221576%22%3A1%2C%22936%22%3A1%2C%221448%22%3A1%2C%221194%22%3A0%2C%221579%22%3A0%2C%221197%22%3A1%2C%221582%22%3A0%2C%221457%22%3A1%2C%221585%22%3A0%2C%22946%22%3A0%2C%221591%22%3A0%2C%22951%22%3A0%2C%221081%22%3A1%2C%221340%22%3A1%2C%221469%22%3A1%2C%221597%22%3A1%2C%221086%22%3A0%2C%221472%22%3A0%2C%221600%22%3A1%2C%221346%22%3A1%2C%221475%22%3A0%2C%221603%22%3A0%2C%22836%22%3A1%2C%221349%22%3A1%2C%221355%22%3A1%2C%221484%22%3A1%2C%221358%22%3A0%2C%221232%22%3A0%2C%221235%22%3A1%2C%221493%22%3A0%2C%221496%22%3A0%2C%221499%22%3A1%2C%221508%22%3A1%2C%221382%22%3A0%2C%221511%22%3A1%2C%221514%22%3A1%2C%22876%22%3A1%2C%221517%22%3A1%2C%221262%22%3A0%2C%22752%22%3A1%2C%221520%22%3A0%2C%221139%22%3A0%2C%221523%22%3A1%2C%221268%22%3A1%2C%221526%22%3A1%2C%221016%22%3A0%2C%221529%22%3A0%2C%221403%22%3A0%2C%221406%22%3A0%2C%221535%22%3A1%7D',
    'originalsource': 'https%3A%2F%2Fwww.google.com%2F',
    'remarketing': 'TypeB',
    'ntfPopupSuppressionCount': '49',
    'userClosedNtfDialogCount': '1',
    'userLastSeenNtfDialogDate': '2022-10-26',
    'userSeenNtfDialogDate': '2022-11-02',
    '_ttgclid': 'EAIaIQobChMI_4jNhN7_-gIVyzArCh1-ewoeEAAYASAAEgLQjfD_BwE',
    '_ttgclid': 'EAIaIQobChMI_4jNhN7_-gIVyzArCh1-ewoeEAAYASAAEgLQjfD_BwE',
    '_ga_9Z139SMQQ8': 'GS1.1.1667452690.13.1.1667456944.60.0.0',
    '_ga': 'GA1.2.1465283199.1666850476',
    'requestBrowserIdMapping': '1',
    'visitor-cookie1': 'true',
    'visitor-cookie30': 'true',
    '_tt_enable_cookie': '1',
    '_ttp': 'c5f16c42-432b-4aad-bdce-7c1125b24fcb',
    '_gac_UA-319064-1': '1.1666850477.EAIaIQobChMI_4jNhN7_-gIVyzArCh1-ewoeEAAYASAAEgLQjfD_BwE',
    '_pxvid': 'de4255e6-55bc-11ed-97ef-6f775a594d6d',
    'RT': '"z=1&dm=revolve.com&si=b533ca70-7eba-4ae6-a8b9-4340fe783e44&ss=la0ma18j&sl=k&tt=cept&bcn=%2F%2F684d0d47.akstat.io%2F&nu=68iyt95&cl=2j74b"',
    '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22w0rOVZsDVBrfOYpTMjqn%22%7D',
    '_px_f394gi7Fvmc43dfg_user_id': 'YzVkNGJlYTAtNTViYy0xMWVkLTkwMzItMjEzOWFlZTc0ODkz',
    '_gcl_aw': 'GCL.1666850478.EAIaIQobChMI_4jNhN7_-gIVyzArCh1-ewoeEAAYASAAEgLQjfD_BwE',
    '_gcl_dc': 'GCL.1666850478.EAIaIQobChMI_4jNhN7_-gIVyzArCh1-ewoeEAAYASAAEgLQjfD_BwE',
    '_gcl_au': '1.1.1434393155.1666850478',
    'cjConsent': 'MHxOfDB8Tnww',
    'cjUser': '146dda99-c4fa-4138-873c-87c7a29264cc',
    'lastRskxRun': '1667455652146',
    'rskxRunCookie': '0',
    'rCookie': 'lwa0twi1hu21xg0xrc7e8l9qnqlhc',
    '_fbp': 'fb.1.1666850481805.848132850',
    'SSP_AB_StyleFinder_20160425': 'Test',
    'SSP_AB_876878223': 'test1',
    '_sp_id.9084': 'd4e040c9-d4a6-418d-bae1-e3f67328b435.1666850497.10.1667455652.1667400522.f5e6e0db-1dcd-4830-b51f-136109ddd1da',
    'name.cookie.last.visited.product': 'AAYR-WD79',
    'product-zoom-appeared': 'true',
    'pageSize': '100',
    '__cflb': '02DiuGfL32DoVPtfcS6ScRNg9KGTvN7R13FSZJAFEDNDi',
    '_gid': 'GA1.2.1645830250.1667399620',
    'requestSessionID': '4535139727',
    'GA_encodeUtmz': 'null',
    'GA_encodeUtma': 'null',
    'JSESSIONID2': '7FF6A32E621B1DE9495E83DA79B57911.tc-fuerte_tomcat4',
    'sortByR2': 'featured',
    'bb_PageURL': '%2Fcontent%2Fnav%2Fpersonalised-designer-list',
    '__cf_bm': 'r6St0rK7dnwAAk87HQIyk9iFouFoNhnkmpqAbKwqA4c-1667456468-0-ASgOdxrPb0cB/zD68d5fqqYsvVyqdW3kfCU1SNZDM1O6edKsSXyI+FgfIRpz61ENueoY6P+YusLa67YiYhn4fAQ=',
    'pxcts': '08c29f5a-5b37-11ed-9b50-685974544a75',
    '_px2': 'eyJ1IjoiY2MzNjgwOTAtNWIzZC0xMWVkLWE1OWUtZDdhYzQ0ZmQ5ZjhjIiwidiI6ImRlNDI1NWU2LTU1YmMtMTFlZC05N2VmLTZmNzc1YTU5NGQ2ZCIsInQiOjE2Njc0NTcyMTA3MjYsImgiOiI4NzRhYWUxNTRjMjYzZjlmN2EwMjU5ODA4Y2Q3MWNlMDEwZTQwZmNmN2NjN2Y5MDI1NGYwZTQwYjBlMTA5MjU1In0=',
    '_sp_ses.9084': '*',
    '_uetsid': '5b6457105abb11eda5d5778f1a8784e3',
    '_uetvid': 'c623f41055bc11edb3a05d0c5c762448',
    'browserID': 'aXxTbOH1r97dqKALQ5vrNqCtrYQMIZ',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.revolve.com/dresses/br/a8e981/?navsrc=main&pageNum=3',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'viewNumR1=100; isPopupEnabledR1=true; pocketViewR1=front; sourcetracking=google; sourcetrackingdate=1666850517250; currency=USD; currencyOverride=INR; userLanguagePref=en; fontsLoaded=1; altexp=%7B%22896%22%3A0%2C%221283%22%3A1%2C%221412%22%3A1%2C%221157%22%3A1%2C%221031%22%3A1%2C%221543%22%3A0%2C%221546%22%3A1%2C%221549%22%3A0%2C%221552%22%3A0%2C%221424%22%3A1%2C%221298%22%3A0%2C%221555%22%3A0%2C%221558%22%3A0%2C%221430%22%3A0%2C%221304%22%3A0%2C%221561%22%3A0%2C%221433%22%3A0%2C%221179%22%3A1%2C%221436%22%3A0%2C%221567%22%3A1%2C%221439%22%3A0%2C%221570%22%3A1%2C%221442%22%3A1%2C%221573%22%3A1%2C%22677%22%3A1%2C%221445%22%3A1%2C%221576%22%3A1%2C%22936%22%3A1%2C%221448%22%3A1%2C%221194%22%3A0%2C%221579%22%3A0%2C%221197%22%3A1%2C%221582%22%3A0%2C%221457%22%3A1%2C%221585%22%3A0%2C%22946%22%3A0%2C%221591%22%3A0%2C%22951%22%3A0%2C%221081%22%3A1%2C%221340%22%3A1%2C%221469%22%3A1%2C%221597%22%3A1%2C%221086%22%3A0%2C%221472%22%3A0%2C%221600%22%3A1%2C%221346%22%3A1%2C%221475%22%3A0%2C%221603%22%3A0%2C%22836%22%3A1%2C%221349%22%3A1%2C%221355%22%3A1%2C%221484%22%3A1%2C%221358%22%3A0%2C%221232%22%3A0%2C%221235%22%3A1%2C%221493%22%3A0%2C%221496%22%3A0%2C%221499%22%3A1%2C%221508%22%3A1%2C%221382%22%3A0%2C%221511%22%3A1%2C%221514%22%3A1%2C%22876%22%3A1%2C%221517%22%3A1%2C%221262%22%3A0%2C%22752%22%3A1%2C%221520%22%3A0%2C%221139%22%3A0%2C%221523%22%3A1%2C%221268%22%3A1%2C%221526%22%3A1%2C%221016%22%3A0%2C%221529%22%3A0%2C%221403%22%3A0%2C%221406%22%3A0%2C%221535%22%3A1%7D; originalsource=https%3A%2F%2Fwww.google.com%2F; remarketing=TypeB; ntfPopupSuppressionCount=49; userClosedNtfDialogCount=1; userLastSeenNtfDialogDate=2022-10-26; userSeenNtfDialogDate=2022-11-02; _ttgclid=EAIaIQobChMI_4jNhN7_-gIVyzArCh1-ewoeEAAYASAAEgLQjfD_BwE; _ttgclid=EAIaIQobChMI_4jNhN7_-gIVyzArCh1-ewoeEAAYASAAEgLQjfD_BwE; _ga_9Z139SMQQ8=GS1.1.1667452690.13.1.1667456944.60.0.0; _ga=GA1.2.1465283199.1666850476; requestBrowserIdMapping=1; visitor-cookie1=true; visitor-cookie30=true; _tt_enable_cookie=1; _ttp=c5f16c42-432b-4aad-bdce-7c1125b24fcb; _gac_UA-319064-1=1.1666850477.EAIaIQobChMI_4jNhN7_-gIVyzArCh1-ewoeEAAYASAAEgLQjfD_BwE; _pxvid=de4255e6-55bc-11ed-97ef-6f775a594d6d; RT="z=1&dm=revolve.com&si=b533ca70-7eba-4ae6-a8b9-4340fe783e44&ss=la0ma18j&sl=k&tt=cept&bcn=%2F%2F684d0d47.akstat.io%2F&nu=68iyt95&cl=2j74b"; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22w0rOVZsDVBrfOYpTMjqn%22%7D; _px_f394gi7Fvmc43dfg_user_id=YzVkNGJlYTAtNTViYy0xMWVkLTkwMzItMjEzOWFlZTc0ODkz; _gcl_aw=GCL.1666850478.EAIaIQobChMI_4jNhN7_-gIVyzArCh1-ewoeEAAYASAAEgLQjfD_BwE; _gcl_dc=GCL.1666850478.EAIaIQobChMI_4jNhN7_-gIVyzArCh1-ewoeEAAYASAAEgLQjfD_BwE; _gcl_au=1.1.1434393155.1666850478; cjConsent=MHxOfDB8Tnww; cjUser=146dda99-c4fa-4138-873c-87c7a29264cc; lastRskxRun=1667455652146; rskxRunCookie=0; rCookie=lwa0twi1hu21xg0xrc7e8l9qnqlhc; _fbp=fb.1.1666850481805.848132850; SSP_AB_StyleFinder_20160425=Test; SSP_AB_876878223=test1; _sp_id.9084=d4e040c9-d4a6-418d-bae1-e3f67328b435.1666850497.10.1667455652.1667400522.f5e6e0db-1dcd-4830-b51f-136109ddd1da; name.cookie.last.visited.product=AAYR-WD79; product-zoom-appeared=true; pageSize=100; __cflb=02DiuGfL32DoVPtfcS6ScRNg9KGTvN7R13FSZJAFEDNDi; _gid=GA1.2.1645830250.1667399620; requestSessionID=4535139727; GA_encodeUtmz=null; GA_encodeUtma=null; JSESSIONID2=7FF6A32E621B1DE9495E83DA79B57911.tc-fuerte_tomcat4; sortByR2=featured; bb_PageURL=%2Fcontent%2Fnav%2Fpersonalised-designer-list; __cf_bm=r6St0rK7dnwAAk87HQIyk9iFouFoNhnkmpqAbKwqA4c-1667456468-0-ASgOdxrPb0cB/zD68d5fqqYsvVyqdW3kfCU1SNZDM1O6edKsSXyI+FgfIRpz61ENueoY6P+YusLa67YiYhn4fAQ=; pxcts=08c29f5a-5b37-11ed-9b50-685974544a75; _px2=eyJ1IjoiY2MzNjgwOTAtNWIzZC0xMWVkLWE1OWUtZDdhYzQ0ZmQ5ZjhjIiwidiI6ImRlNDI1NWU2LTU1YmMtMTFlZC05N2VmLTZmNzc1YTU5NGQ2ZCIsInQiOjE2Njc0NTcyMTA3MjYsImgiOiI4NzRhYWUxNTRjMjYzZjlmN2EwMjU5ODA4Y2Q3MWNlMDEwZTQwZmNmN2NjN2Y5MDI1NGYwZTQwYjBlMTA5MjU1In0=; _sp_ses.9084=*; _uetsid=5b6457105abb11eda5d5778f1a8784e3; _uetvid=c623f41055bc11edb3a05d0c5c762448; browserID=aXxTbOH1r97dqKALQ5vrNqCtrYQMIZ',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'aliasURL': 'dresses/br/a8e981',
    's': 'c',
    'c': 'Dresses',
    'navsrc': 'main',
    'pageNum': '3',
}

response = requests.get('https://www.revolve.com/r/BrandsContent.jsp', params=params, cookies=cookies, headers=headers)
print(response.url)

soup=bs(response.text,'html.parser')
l=[]
d={}

products=soup.find_all('li','js-plp-container')
print(products)
for product in products:
    name=product.find('div','product-name u-margin-t--lg js-plp-name').text
    brand=product.find('div','product-brand u-margin-b--sm js-plp-brand').text
    price=product.find('div','price js-plp-prices-div').find('span').text
    seller=product.find('span','image-badge__text').text
    seller_link=product.find('a','pill-badges--sm')
    image=product.find('img','products-grid__image-link-img plp-image js-plp-image')
    

    d = {'name':name,'brand':brand,'price':price,'seller':seller,'seller_link':seller_link,'image':image}
    # print(d)
    l.append(d)
    df=pd.DataFrame(l)
    df.to_excel('revolves.xlsx')