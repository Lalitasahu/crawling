import requests
import re
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import Session
import json
s=Session()
# s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
cookies = {
    '_abck': 'AE74EF5865276C475CF2A65EA7DC0905~0~YAAQn2PUF+Uvi5+EAQAActl2vAjD4/VgkCNXHCt0WVEVJ4ICsrhUqafpolnOzpUFPhb2AFAFb+yapZiJIxAcM+ucTrrpUEHFR84A31iEhPelMeY/bl81tpa2BLffK3UMv2cGxZqfgLXwX6oRX5VpBbrDudfL1FWydOaBLCVTKDk2eCSp8N5+oQONTOKViGRw8sUTQ4t0in9MvHxcDuavIZq664ewLHhBiItyT1s3k8h7H1U7DV9B1umUkxfYm2SKiCKI5eoVJmPcJV+pkKv5LzQZwiJIUz78kTlCc3abpzW3p0MBDX0POfP59BbPL5sbC+VddXIMygDaKhhgN0JohxMrExFjwHrSe4jasy1bw+thyxAjIacKnSDwr0YlQtBG/OafzW5sZ5imjOBjPJywauvKbE0KBlgxCA==~-1~-1~1669612756',
    'at': 'ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWlRjM1pXRXhabVl0TXpoallTMHhNV1ZrTFdKak5ESXROekppT1dObE5HWTNNbUk0SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUyTnpreU1UazVOak1zSW1semN5STZJa2xFUlVFaWZRLkUzOHRILVhMNTFKWUcxOWdVdzdMZ2VlSkwyd01ndGR4ZTBhVEItS2xPdkk=',
    'utrid': 'VVleCH1jeB1xWExmY2VAMCMyNjQ4OTg3NDU1JDI%3D.d09d9cb7462f0ce06b40c300d278984c',
    '_d_id': 'f627e5d3-243f-4396-aa41-e654ce8c5923',
    'mynt-eupv': '1',
    '_xsrf': 'rZb1Hmpc5DFdyKi0CgA8QMWJFB8PtWYS',
    '_gcl_au': '1.1.801072838.1663667990',
    'mynt-ulc-api': 'pincode%3A110003',
    'mynt-loc-src': 'expiry%3A1669610560365%7Csource%3AIP',
    '_fbp': 'fb.1.1663667992655.1646871842',
    '_ga': 'GA1.2.847808827.1663667993',
    'tvc_VID': '1',
    'cto_bundle': 'SqKJwV80WldtVmwzaTZKT2pjdllINGVCRDFoTVJTWWJXcHpDU21XS2FIb0hTJTJGUVMlMkZtdFNQUkxERHdiMFR1RmxoRjNwRk1XbG9lV2RtY0RnSXB1WWMlMkZkTXVXblozQTVzNmZ5YWU2OWtQOEVidjZqa09YMWpxRVUwYkJJUkNhNEp4WDFPcmk0cjZiUmVkMXNxVVhZSm5vJTJCMiUyRjBBJTNEJTNE',
    '_cc_id': 'ebb7aebe075a81cd7a32979f0bb52bdc',
    'trackmyvisits': '2fe86bafe0532',
    'ak_RT': '"z=1&dm=myntra.com&si=13c5a365-1cd4-41ae-bbec-d9410702cf5f&ss=lb0a4cl6&sl=3&tt=1noe&obo=1&rl=1"',
    '_gcl_aw': 'GCL.1668793374.Cj0KCQiA99ybBhD9ARIsALvZavXemLpLl2QPQIrxhAXgeRVYQBcWdYumnveNO_YLqCClN9SGsaOss-UaAlqxEALw_wcB',
    'OMG-349836': 'SSKey=&UUserID={71667a87-8b0b-45f5-be87-52b04288b0ca}&fpc=true&attributionMode=fpc&AttributionPartnerRef=Cj0KCQiA99ybBhD9ARIsALvZavXemLpLl2QPQIrxhAXgeRVYQBcWdYumnveNO_YLqCClN9SGsaOss-UaAlqxEALw_wcB&channel=dms_google',
    '_gac_UA-1752831-18': '1.1668793376.Cj0KCQiA99ybBhD9ARIsALvZavXemLpLl2QPQIrxhAXgeRVYQBcWdYumnveNO_YLqCClN9SGsaOss-UaAlqxEALw_wcB',
    '_gid': 'GA1.2.1761707093.1669532023',
    '_mxab_': 'config.bucket%3Dregular%3Bcheckout.donation%3Denabled%3Bcheckout.share%3Ddisabled%3Bpdp.expiry.date%3Denabled%3Bshl.desktop%3Denabled-1',
    '_pv': 'default',
    'dp': 'd',
    'utm_track_v1': '%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1669609357%2C%22trackend%22%3A1669609417%7D',
    'lt_timeout': '1',
    'lt_session': '1',
    'AKA_A2': 'A',
    'ak_bmsc': '3D0259778C5BBBBBD5F6AFA40DB0092E~000000000000000000000000000000~YAAQn2PUFxEwi5+EAQAAPtt2vBGRchoJdOYd7NNdwq7F2O+9bshTdXXDtphXvREndcZqsWsDG5Lrivf2687FIXNQQ3l5g472xNPMdKNz+HoxyWDt3KNiu5rh9o+Jsa6E64ZWaOpEkJ6ViZq+/P8DqApXHoLPtxZieQAAcEFXKwwvrxoOEWm/At+E+qeV2nqMVIX3JfvE5uERKBAUsOri5QVwrklJ/8NuSJvrdxAHkE4mcSsSiUSK7rxRAMuMiYf3O5P9K9ktdT9nIrJ3raoP6ZWsg1uIMIJHRo7uKWYPqSEygnOJsAllAgY3w98h5IbHH3WFrlXd5YG9ICPOZ6+v1fVD36Von+dh0cAJ659F/NkSIgoyOrk0PjE3W6icp0MdBOw7JikUiPUsPHH++JdmnPmaQy4T8B+soR0bryXFEQ4VzgEXVDST2ld5P+ZbmokDpJrxWgC/AFwjcqOmIM8j3uCBTeVjyN4h4OYTKwvws8kHNCp12QIYBMO7lHk=',
    'bm_sz': '2DDE0F15A66CB86C6367FF432B70E3C4~YAAQn2PUF7Evi5+EAQAA7dZ2vBF3m08zoin0aH5QmnjoUzgOk+sMhpcKwsnKA527BaUflrjNs8D7y+buk78OiZQkEMM8oHbVaQJYcbUvzcS+trPjWFcyeFMdIXKTezOlRVH115BFFsaXeeFwDu5PZxqql9S41bmBAqOvpFGVRT4ZaBtmoBDiNe9jLXcPF8NzvuqQfCeMrCfqQtpCxRjmGl7xqxqBwIQnzZzVXC0Dq1p9er+/J1I3UURaxEDsj8mz2csABOXpG2rQfeuSGlG1vgyRKOtCFdPdN4emKt0uGyYMMAU=~3490873~4534849',
    '_ma_session': '%7B%22id%22%3A%22e817ed6f-a582-4221-8f3d-f13b39d7e697-f627e5d3-243f-4396-aa41-e654ce8c5923%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D',
    'microsessid': '583',
    'user_session': 'mO2lm62PKP20_CJ9bla_vg.uoFes0K3e9_pTMTGLGuA_L6q_3UlnWIqLjpgl64tReb6ocn20YU0BICoIhJIABP1hcHGpqeJ-Fsq1_fQMHwEKcKL58UZMmSf1v2cu5zB9TB7RPNmHOClf4o8Qyc1ww9CHS8sL7PufwbzjelCpaQE0w.1669609216301.86400000.0T1YUFTR2DB-6BP5WtLBsgbFEfoupLhlUpCA7IGuapM',
    'bm_sv': '6DF8CEFDA5055EE1E535D85F01A7BDCC~YAAQn2PUF5tmi5+EAQAAPDh5vBEfCCZZqGJ0Z4Uly2IjzoATitNebkJpZmeVlwl3AQhrS7yAt33qguin0e1NPFUdxFaNl1rwr23SasO7ch+CyB7/geP7YlL3+BboHd8b+7IZ3luhqUAyNExt35KmsJmwYNFbLuCpgHwnrg7jfO4pmn2WBcjmdSZ2paZbwEfXeIUGVPuIO/adyq2kjjKDB5kSy9RBQvMJ8h67SNqIJwjFK46c/h5m0Zyd9GxL8J4DIA==~1',
    'AMP_TOKEN': '%24NOT_FOUND',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.myntra.com/reviews/7030192',
    'X-myntraweb': 'Yes',
    'X-Requested-With': 'browser',
    'x-location-context': 'pincode=110003;source=IP',
    'x-meta-app': 'deviceId=f627e5d3-243f-4396-aa41-e654ce8c5923;appFamily=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0;reqChannel=web;channel=web;',
    'deviceId': 'f627e5d3-243f-4396-aa41-e654ce8c5923',
    'Content-Type': 'application/json',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_abck=AE74EF5865276C475CF2A65EA7DC0905~0~YAAQn2PUF+Uvi5+EAQAActl2vAjD4/VgkCNXHCt0WVEVJ4ICsrhUqafpolnOzpUFPhb2AFAFb+yapZiJIxAcM+ucTrrpUEHFR84A31iEhPelMeY/bl81tpa2BLffK3UMv2cGxZqfgLXwX6oRX5VpBbrDudfL1FWydOaBLCVTKDk2eCSp8N5+oQONTOKViGRw8sUTQ4t0in9MvHxcDuavIZq664ewLHhBiItyT1s3k8h7H1U7DV9B1umUkxfYm2SKiCKI5eoVJmPcJV+pkKv5LzQZwiJIUz78kTlCc3abpzW3p0MBDX0POfP59BbPL5sbC+VddXIMygDaKhhgN0JohxMrExFjwHrSe4jasy1bw+thyxAjIacKnSDwr0YlQtBG/OafzW5sZ5imjOBjPJywauvKbE0KBlgxCA==~-1~-1~1669612756; at=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWlRjM1pXRXhabVl0TXpoallTMHhNV1ZrTFdKak5ESXROekppT1dObE5HWTNNbUk0SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUyTnpreU1UazVOak1zSW1semN5STZJa2xFUlVFaWZRLkUzOHRILVhMNTFKWUcxOWdVdzdMZ2VlSkwyd01ndGR4ZTBhVEItS2xPdkk=; utrid=VVleCH1jeB1xWExmY2VAMCMyNjQ4OTg3NDU1JDI%3D.d09d9cb7462f0ce06b40c300d278984c; _d_id=f627e5d3-243f-4396-aa41-e654ce8c5923; mynt-eupv=1; _xsrf=rZb1Hmpc5DFdyKi0CgA8QMWJFB8PtWYS; _gcl_au=1.1.801072838.1663667990; mynt-ulc-api=pincode%3A110003; mynt-loc-src=expiry%3A1669610560365%7Csource%3AIP; _fbp=fb.1.1663667992655.1646871842; _ga=GA1.2.847808827.1663667993; tvc_VID=1; cto_bundle=SqKJwV80WldtVmwzaTZKT2pjdllINGVCRDFoTVJTWWJXcHpDU21XS2FIb0hTJTJGUVMlMkZtdFNQUkxERHdiMFR1RmxoRjNwRk1XbG9lV2RtY0RnSXB1WWMlMkZkTXVXblozQTVzNmZ5YWU2OWtQOEVidjZqa09YMWpxRVUwYkJJUkNhNEp4WDFPcmk0cjZiUmVkMXNxVVhZSm5vJTJCMiUyRjBBJTNEJTNE; _cc_id=ebb7aebe075a81cd7a32979f0bb52bdc; trackmyvisits=2fe86bafe0532; ak_RT="z=1&dm=myntra.com&si=13c5a365-1cd4-41ae-bbec-d9410702cf5f&ss=lb0a4cl6&sl=3&tt=1noe&obo=1&rl=1"; _gcl_aw=GCL.1668793374.Cj0KCQiA99ybBhD9ARIsALvZavXemLpLl2QPQIrxhAXgeRVYQBcWdYumnveNO_YLqCClN9SGsaOss-UaAlqxEALw_wcB; OMG-349836=SSKey=&UUserID={71667a87-8b0b-45f5-be87-52b04288b0ca}&fpc=true&attributionMode=fpc&AttributionPartnerRef=Cj0KCQiA99ybBhD9ARIsALvZavXemLpLl2QPQIrxhAXgeRVYQBcWdYumnveNO_YLqCClN9SGsaOss-UaAlqxEALw_wcB&channel=dms_google; _gac_UA-1752831-18=1.1668793376.Cj0KCQiA99ybBhD9ARIsALvZavXemLpLl2QPQIrxhAXgeRVYQBcWdYumnveNO_YLqCClN9SGsaOss-UaAlqxEALw_wcB; _gid=GA1.2.1761707093.1669532023; _mxab_=config.bucket%3Dregular%3Bcheckout.donation%3Denabled%3Bcheckout.share%3Ddisabled%3Bpdp.expiry.date%3Denabled%3Bshl.desktop%3Denabled-1; _pv=default; dp=d; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1669609357%2C%22trackend%22%3A1669609417%7D; lt_timeout=1; lt_session=1; AKA_A2=A; ak_bmsc=3D0259778C5BBBBBD5F6AFA40DB0092E~000000000000000000000000000000~YAAQn2PUFxEwi5+EAQAAPtt2vBGRchoJdOYd7NNdwq7F2O+9bshTdXXDtphXvREndcZqsWsDG5Lrivf2687FIXNQQ3l5g472xNPMdKNz+HoxyWDt3KNiu5rh9o+Jsa6E64ZWaOpEkJ6ViZq+/P8DqApXHoLPtxZieQAAcEFXKwwvrxoOEWm/At+E+qeV2nqMVIX3JfvE5uERKBAUsOri5QVwrklJ/8NuSJvrdxAHkE4mcSsSiUSK7rxRAMuMiYf3O5P9K9ktdT9nIrJ3raoP6ZWsg1uIMIJHRo7uKWYPqSEygnOJsAllAgY3w98h5IbHH3WFrlXd5YG9ICPOZ6+v1fVD36Von+dh0cAJ659F/NkSIgoyOrk0PjE3W6icp0MdBOw7JikUiPUsPHH++JdmnPmaQy4T8B+soR0bryXFEQ4VzgEXVDST2ld5P+ZbmokDpJrxWgC/AFwjcqOmIM8j3uCBTeVjyN4h4OYTKwvws8kHNCp12QIYBMO7lHk=; bm_sz=2DDE0F15A66CB86C6367FF432B70E3C4~YAAQn2PUF7Evi5+EAQAA7dZ2vBF3m08zoin0aH5QmnjoUzgOk+sMhpcKwsnKA527BaUflrjNs8D7y+buk78OiZQkEMM8oHbVaQJYcbUvzcS+trPjWFcyeFMdIXKTezOlRVH115BFFsaXeeFwDu5PZxqql9S41bmBAqOvpFGVRT4ZaBtmoBDiNe9jLXcPF8NzvuqQfCeMrCfqQtpCxRjmGl7xqxqBwIQnzZzVXC0Dq1p9er+/J1I3UURaxEDsj8mz2csABOXpG2rQfeuSGlG1vgyRKOtCFdPdN4emKt0uGyYMMAU=~3490873~4534849; _ma_session=%7B%22id%22%3A%22e817ed6f-a582-4221-8f3d-f13b39d7e697-f627e5d3-243f-4396-aa41-e654ce8c5923%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D; microsessid=583; user_session=mO2lm62PKP20_CJ9bla_vg.uoFes0K3e9_pTMTGLGuA_L6q_3UlnWIqLjpgl64tReb6ocn20YU0BICoIhJIABP1hcHGpqeJ-Fsq1_fQMHwEKcKL58UZMmSf1v2cu5zB9TB7RPNmHOClf4o8Qyc1ww9CHS8sL7PufwbzjelCpaQE0w.1669609216301.86400000.0T1YUFTR2DB-6BP5WtLBsgbFEfoupLhlUpCA7IGuapM; bm_sv=6DF8CEFDA5055EE1E535D85F01A7BDCC~YAAQn2PUF5tmi5+EAQAAPDh5vBEfCCZZqGJ0Z4Uly2IjzoATitNebkJpZmeVlwl3AQhrS7yAt33qguin0e1NPFUdxFaNl1rwr23SasO7ch+CyB7/geP7YlL3+BboHd8b+7IZ3luhqUAyNExt35KmsJmwYNFbLuCpgHwnrg7jfO4pmn2WBcjmdSZ2paZbwEfXeIUGVPuIO/adyq2kjjKDB5kSy9RBQvMJ8h67SNqIJwjFK46c/h5m0Zyd9GxL8J4DIA==~1; AMP_TOKEN=%24NOT_FOUND',
}

params = {
    'size': '12',
    'sort': '0',
    'rating': '0',
    'page': '4',
    'includeMetaData': 'true',
}
s.headers.update(headers)


allreview = []
def reviews(url):
    response = requests.get('https://www.myntra.com/gateway/v1/reviews/product/7030192', params=params, cookies=cookies, headers=headers)
    response.json()
    js=response.json()
    print(url)
    review=js['reviews']
    for r in review:
        id = r.get('style').get('id')
        userName = r.get('userName')
        rating  = r.get('userRating')
        like = r.get('upvotes')
        dislike = r.get('downvotes')
        data = r.get('updatedAt')
        view = r.get('review')
        images=js['reviewsMetaData']['images']
        image = []
        for i in images:
            img = i.get('url')
            image.append(img)

        rews={'id':id,
            'userName':userName,
            'rating':rating,
            'review_url':url,
            'like':like,
            'dislike':dislike,
            'view':view,
            'data': data
        
            }
        allreview.append(rews)
    # print(allreview)
    return allreview


    # https://regex101.com/
    # try:
    #     id=re.search('"id":(.*?),',r.text).group(1)
    # except:
    #     id='NA'
    
    # try:
    #     Name=re.search('"userName":"(.*?)",',r.text).group(1)
    # except:
    #     Name='NA'
    # try:
    #     review=re.search('"review":"(.*?)"',r.text).group(1)
    # except:
    #     review="no review"

    # try:  
    #     rating=re.search('"userRating":(.*?),',r.text).group(1)
    # except:
    #     rating='NA'
    
    # try:
    #     totalCountraiting=re.search('"totalCount":(.*?),',r.text).group(1)
    # except:
    #     totalCountraiting='NA'

    # try:
    #     upvotes=re.search('"upvotes":"(.*?)"',r.text).group(1)
    # except:
    #     upvotes="NA"

    # try:
    #     image=re.search('"upvotes":"(.*?)"',r.text).group(1)
    # except:
    #     image='NA'

def crawl_detail(url):
    r=s.get(url)
    # print(url)

    
    try:
        brand=re.search('"brand":"(.*?)"',r.text).group(1)
    except:
        brand='NA'

    try:
        name=re.search('"name":"(.*?)"',r.text).group(1)
    except:
        name='NA'

    try:
        images='||'.join(re.findall('{"src":"(.*?)",',r.text.replace('u002F','').replace('\\','/').replace('($height)','720').replace('($qualityPercentage)','90').replace('($width)','540')))
    except:
        images='NA'
   
    try:
        userName='||'.join(re.findall('"userName":(.*?),',r.text))
    except:
        userName='NA'

    try:
        specifications = json.loads(re.search('articleAttributes":(.*?),"systemAttr',r.text).group(1))
        sp = {}
        for i in specifications:
            if specifications[i] != 'NA':
                sp[i] = specifications[i]   
    except :
        sp = {}

    try:
        id='https://www.myntra.com/reviews/'+re.search('"id":(.*?),',r.text).group(1)
    except:
        id='NA'
    
    review_fun=reviews(id)

    data={'brand':brand,
         'name':name,
         'images':images,         
         'userName':userName,
         'specification':sp,
         'reviews':review_fun
        #  'Specifications':Specifications,
        #  'CompleteTheLook':CompleteTheLook,
         
         }
    # data.update(sp)
    return data

all_Data=[]
pro_Link=[]
def crawl_list(url):
    # url='https://www.myntra.com/men-tshirts'
   
    next_page=url
    while next_page:
        r=s.get(next_page)
        print(r)
        soup=bs(r.text,'html.parser')
        link=re.findall('"landingPageUrl":"(.*?)",',r.text.replace('u002F','').replace('\\','/'))
        for l in link:
            links='https://www.myntra.com/'+l
            # pro_Link.append(links)
            detail=crawl_detail(links)
            d={'links':links}
            d.update(detail)
            print(d)
            all_Data.append(d)
        if soup.find('link',attrs={'rel':'next'}):
            next_page=soup.find('link',attrs={'rel':'next'}).get('href')
            print(f'THIS IS NEXT PAGE.. {next_page}.......................')
        else:
            next_page=False



# url='https://www.myntra.com/rain-jacket'
url=['https://www.myntra.com/hair-dryer','https://www.myntra.com/rain-jacket']
for i in url:
    crawl_list(i)
    # reviews(url)

df=pd.DataFrame(allreview)
df.to_excel('final.xlsx',index=False)

df=pd.DataFrame(all_Data)
df.to_excel('final.xlsx',index=False)
print(all_Data)

