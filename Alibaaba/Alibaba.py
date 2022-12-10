import re
import json
import requests
import pandas as pd
from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html
s = Session()




cookies = {
    't': '8f18817fc995d73bdc1c3b55e02e70a2',
    'ali_apache_id': '33.2.245.202.166366887718.361358.0',
    'ali_apache_track': '""',
    '_bl_uid': '74l8h8tea5211sizscgmh4pl0XRt',
    'xman_us_f': 'x_l=1',
    'xman_f': '9yGAzUuOO0QSnV30at2l7Y/JIWN+8B1jyiDw6Cb2LcsdzMPMHApU3Kqw/Ik1KuoHGpr1PFAoK/z/fBMuXWyajaBlWNSldeRAZgH9+9WSADRehoNBPB71WQ==',
    'cna': 'joCwG4fuLDICAWdFGIDnFrYQ',
    'isg': 'BJSUSe29i8zauR-iTMNEj_CvZtIG7bjXpulFeC51IJ-iGTRjVv2IZ0qYGYmB-vAv',
    'l': 'fBI4ilGPTaYCEXyOBOfanurza77OSIOYYuPzaNbMi9fP_M1M5QOPW65MS4THC36NFs_MR3oXCczJBeYBq3K-nxv9kloV96HmndLHR35..',
    'tfstk': 'cCedBxZGNNb335cIbvCi4nXHqNPRChtKrHgJe-CAVe-FIsVLOJ10N-2YSl5I4qudX',
    '_ga': 'GA1.2.613400981.1663668908',
    'intl_locale': 'en_US',
    'sc_g_cfg_f': 'sc_b_locale=en_US&sc_b_currency=INR&sc_b_site=IN',
    '__wpkreporterwid_': '5fa7aa33-0925-4596-24e9-0c78da2ae952',
    'ug_se_c': 'free_1670082850127',
    'uns_unc_f': 'trfc_i=ppc^p1h0jag9^^1gjc0rn7f^ggs_ggl',
    '_m_h5_tk': 'f6702601f5a057d74708ba82f52af16c_1670085255409',
    '_m_h5_tk_enc': '7eae7d4ab570bd7e6736e4c27f614eda',
    '_gid': 'GA1.2.1759167601.1670068465',
    'XSRF-TOKEN': '4064c9c0-ad2b-4a8b-bf5c-f454ae78e3d9',
    'ali_apache_tracktmp': '""',
    'cookie2': 's5878a19abd29c6855cc05ce8b3bbae3',
    '_tb_token_': 'e170e3a3610d5',
    'acs_usuc_t': 'acs_rt=75ee2cfc85224607a07870aeb9368b7d',
    'xman_t': 'O/SrEDhqvGZMVd06pTHXTkWQJZ6gprlq7OQC7y5vZOaHBSb2V269dNVagnb2zAR/VKvKo9CSR63VgRMXz623Wp+We+u4ERZK',
    '_samesite_flag_': 'true',
    'JSESSIONID': 'F0F492128FCDCA3951F8D9678D844CC7',
    '_csrf_token': '1670072355671',
}




headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.alibaba.com/product-detail/custom-matte-bronzer-concealer-contour-palette_1600368048812.html?spm=a27aq.industry_category_productlist.dt_2.1.dd194e85qLCrR6',
    'bx-v': '2.2.3',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    # 'Cookie': 't=8f18817fc995d73bdc1c3b55e02e70a2; ali_apache_id=33.2.245.202.166366887718.361358.0; ali_apache_track=""; _bl_uid=74l8h8tea5211sizscgmh4pl0XRt; xman_us_f=x_l=1; xman_f=9yGAzUuOO0QSnV30at2l7Y/JIWN+8B1jyiDw6Cb2LcsdzMPMHApU3Kqw/Ik1KuoHGpr1PFAoK/z/fBMuXWyajaBlWNSldeRAZgH9+9WSADRehoNBPB71WQ==; cna=joCwG4fuLDICAWdFGIDnFrYQ; isg=BJSUSe29i8zauR-iTMNEj_CvZtIG7bjXpulFeC51IJ-iGTRjVv2IZ0qYGYmB-vAv; l=fBI4ilGPTaYCEXyOBOfanurza77OSIOYYuPzaNbMi9fP_M1M5QOPW65MS4THC36NFs_MR3oXCczJBeYBq3K-nxv9kloV96HmndLHR35..; tfstk=cCedBxZGNNb335cIbvCi4nXHqNPRChtKrHgJe-CAVe-FIsVLOJ10N-2YSl5I4qudX; _ga=GA1.2.613400981.1663668908; intl_locale=en_US; sc_g_cfg_f=sc_b_locale=en_US&sc_b_currency=INR&sc_b_site=IN; __wpkreporterwid_=5fa7aa33-0925-4596-24e9-0c78da2ae952; ug_se_c=free_1670082850127; uns_unc_f=trfc_i=ppc^p1h0jag9^^1gjc0rn7f^ggs_ggl; _m_h5_tk=f6702601f5a057d74708ba82f52af16c_1670085255409; _m_h5_tk_enc=7eae7d4ab570bd7e6736e4c27f614eda; _gid=GA1.2.1759167601.1670068465; XSRF-TOKEN=4064c9c0-ad2b-4a8b-bf5c-f454ae78e3d9; ali_apache_tracktmp=""; cookie2=s5878a19abd29c6855cc05ce8b3bbae3; _tb_token_=e170e3a3610d5; acs_usuc_t=acs_rt=75ee2cfc85224607a07870aeb9368b7d; xman_t=O/SrEDhqvGZMVd06pTHXTkWQJZ6gprlq7OQC7y5vZOaHBSb2V269dNVagnb2zAR/VKvKo9CSR63VgRMXz623Wp+We+u4ERZK; _samesite_flag_=true; JSESSIONID=F0F492128FCDCA3951F8D9678D844CC7; _csrf_token=1670072355671',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'jsv': '2.6.1',
    'appKey': '24889839',
    't': '1670231683852',
    'sign': '08f3a7916d2e1aa1d7d3c391838cb0be',
    'api': 'mtop.alibaba.intl.mobile.fp.loadMore',
    'v': '1.0',
    'H5Request': 'true',
    'type': 'jsonp',
    'dataType': 'jsonp',
    'callback': 'mtopjsonp5',
    'data': '{"env":"freepage_pc","endpoint":"pc","appCountry":"IN","channel":"category_home","language":"en","locale":"en_US","aliId":"0","pageIndex":5,"requestUrl":"https://www.alibaba.com/beauty/makeup-tools/p66_p660103","clientIp":"103.216.143.100","cnaId":"joCwG4fuLDICAWdFGIDnFrYQ","appkey":"90","currency":"INR","page":"industry_cate_productlist","paramMap":"{\\"categoryIds\\":\\"660103\\",\\"mainContentKey\\":\\"list\\",\\"traceInfo\\":\\"{\\\\\\"name\\\\\\":\\\\\\"intelligent.product\\\\\\",\\\\\\"params\\\\\\":\\\\\\"floorName,trackInfo\\\\\\"}\\",\\"templateName\\":\\"icbu_dx_category_product_card_24\\",\\"modulePerLine\\":\\"2\\",\\"moduleId\\":\\"500\\"}"}',
}




s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
url ='https://www.alibaba.com/electrical-equipment-supplies/electrical-supplies/p5_p201148509?spm=a2700.details.scGlobalHomeHeader.514.65613620he0hky'
# url = 'https://www.alibaba.com/beauty/makeup-tools/p66_p660103?spm=a2700.7735675.scGlobalHomeHeader.481.3bff63965Ipccw'


def detailpage(url):
    params = {
    # 
        'detailId': url.split("_")[-1].replace('.html',''),
        'language': 'en',
    }    
    print(params)
    response = requests.get('https://www.alibaba.com/event/app/mainAction/desc.htm', params=params, cookies=cookies, headers=headers)
    r = s.get(url)
    js = response.json()
    print(url)
    _tree = html.fromstring(response.text)
    tree = html.fromstring(js['data']['productHtmlDescription'])
    soup = bs(r.text,'html.parser')

    try:
        name = soup.find('div','product-title').text
    except:
        name =''
    try:
        pieces = soup.find('div','quality').text.replace('>=','').strip()
    except:
        pieces = 'NA'

    try:
        price = re.search('"formatPrice":"(.*?)"',r.text).group(1)
    except:
        price = 'NA'
    Benefits = soup.find('span','golden-buyer-first-benefit').text
    sp = json.loads(re.search('"productBasicProperties":(.*?),"productCategoryId"',r.text).group(1))
    specification = {}
    for speci in sp:
        specification[speci['attrName']] = speci['attrValue']

    pro_detailskey = _tree.xpath('//div[@style="box-sizing: content-box; margin: 0px; padding: 5px 10px; border: 0px; font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; vertical-align: baseline; width: 166px; height: auto; overflow: hidden;\"]//text()')
    pro_detailsvalue  = _tree.xpath('//div[@style="box-sizing: content-box; margin: 0px; padding: 5px 10px; border: 0px; font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; vertical-align: baseline; width: 537px; height: auto; overflow: hidden;\"]//text()')
    pro_details = dict(zip(pro_detailskey,pro_detailsvalue))

    image = soup.find_all('div','main-item')
    imgs = []
    for img in image:
        images = img.find('img').get('src').replace('_100x100xz.jpg','')
        imgs.append(images)


    return {
        'Name':name,
        'price':price,
        'pieces':pieces,
        'Benefits':Benefits,
        'specification':specification,
        'pro_details':pro_details,
        'images':'||'.join(imgs)

    }


alldata =[]
def listpage(url):
#   for i in range(1,3):
    # response = requests.get('https://acs.h.alibaba.com/h5/mtop.alibaba.intl.mobile.fp.loadmore/1.0/',params=params, cookies=cookies, headers=headers,)
    r = s.get(url)
    link = re.findall('"detail":"(.*?)"',r.text.replace('\\',''))
    for i in link:
        links = 'https:'+i
        detail = detailpage(links)
        data = {
            'links':links,
        }
        data.update(detail)
        alldata.append(data)

listpage(url)
print(alldata)


df = pd.DataFrame(alldata)
df.to_excel('alibabaother.xlsx',index = False)




https://www.yelp.com/biz/forest-books-san-francisco-2?osq=best+books
https://www.yelp.com/biz/black-bird-bookstore-and-cafe-san-francisco?osq=best+books
https://www.yelp.com/biz/friends-of-the-sf-public-library-annual-big-book-sale-san-francisco?osq=best+books




/adredir?ad_business_id=EOM6CItD6sI5P3a-JV61_Q&campaign_id=XnefWgj_aH6fUFfpwWpYRg&click_origin=search_results&placement=above_search&placement_slot=1&redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fapplebees-grill-bar-san-francisco&request_id=2786b49ae9c1e4ae&signature=bbd54662ecba4c8beffdeed41ddd9cf65b6ffc266d8a6879431c5a3713851afb&slot=0