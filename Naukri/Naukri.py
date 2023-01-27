import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache',
    'appid': '109',
    'systemid': '109',
    'clientid': 'd3skt0p',
    'gid': 'LOCATION,INDUSTRY,EDUCATION,FAREA_ROLE',
    'Connection': 'keep-alive',
    'Referer': 'https://www.naukri.com/wordpress-jobs-4?kk=wordpress',
    'Cookie': '_t_s=seo; _t_sd=google; _t_ds=50842591674539324-75084259-05084259; _t_us=63CFA142; _t_ds=50842591674539324-75084259-05084259; _abck=C7236BCB7ED3641CF4B0FC80CAC4FEC0~-1~YAAQPW0/F4jj8MWFAQAAcO5T4wk0LbqQ0/646y1Y6KwXPzOycukN9Z2Z83Mn45Ze5dKbNKfYvcB2XRhsjClz0dbo0sKpi9HwoUP//ELAinEE3neQYZLE0pRV83uzMKz68a64jN6XTQvQR3t4O6znj7XaDlWM/WQptS2Me0YcihwbmW6Vj/KRHhBn3x24ricbHO302G43VaEYxvX/VjDjVjKNGVMZ4KErHto0mfSKOwmGzwyhNJ5gyMIXX0lMN1U+Hxu5PdT/lskPRc9X52rap5aN+OnQDV1vKF5dnifKqDJiIsMvl5oKwYx+fi+wiZQOz5/tUOcneOYKaVFQmqgG8b9blkzE7BEdzhxRyD+kJHKJcKbTHi17++ZSCKLMQLes~-1~-1~-1; bm_sz=4D8B5BBC2B4924DF4E23013774DB0424~YAAQXG0/F6LYTc6FAQAAiE0b4xLNdjDo9Yf4fCuOANSszchc4JX8aVwGqO0s5e5WXBU/8TWLc0yYFx8K9zsGHm5AQoM3y0CQODU4uX9Xz23sjTDHiFzwkYzpyyJ6ZJ9ws9YheMN2vvQt5/tJmmYm+NCtWbcxjBjFbzt6g/h+biKcORzceuaSm0k7c2KsA3O3k7TpYgstKFGRXzvqbTT/WVjOSW0yx6N95UvE9Uz824JfyYaig4AbZ80vv4MOhY5+vRBSNxy0zuNqx1u2ssnegBtiutd1u0SDETJU3sBw6DRg6hqNczlY56adNUJgDS/uaPOPl9Alh7Kme2A=~4405297~4604473; _gcl_au=1.1.468746179.1674539129; _ga=GA1.2.1133519385.1674539130; _gid=GA1.2.360158656.1674539130; _gac_UA-182658-1=1.1674539130.EAIaIQobChMIgf7dicHf_AIVQzUrCh0bfA7REAAYASAAEgJLmvD_BwE; _fbp=fb.1.1674539131468.239181266; test=naukri.com; _t_s=seo; persona=default; _ga_K2YBNZVRLL=GS1.1.1674551421.2.0.1674551431.0.0.0; __gads=ID=df082f68b752da5b:T=1674539372:S=ALNI_MaTQkC-OKqKTyZxSXcau1exYaWeSA; __gpi=UID=00000bab5bcc30e4:T=1674539372:RT=1674539372:S=ALNI_MZqIdk4cxNXxhcLn087qmrf38NGKg; cto_bundle=qhBnrV9IUElNcjI5UTRjeVJ2aUpsRnJtejhhdnc3biUyRlclMkZhMW5FeElEUkVmbVVCa2sxaDdXdzk2SEMlMkJZZ2hmV0hFc0xKb2REbDFCOTlXN29CMVg1WGlMWiUyRk9zSklRd2t0VU9CQWVqY1BZY2k4bWNWTHNJODhjYzBNVTYxYzlzN3ptQTZoUk1vbHNGWEZKN2ZDTWtFdHlRTSUyQnhBJTNEJTNE; jd=200123004981; _t_sd=google; _t_r=1030%2F%2F; ak_bmsc=0C727E7F77171653A967DD84B80667B0~000000000000000000000000000000~YAAQPW0/F4697sWFAQAAcu8N4xKHFqsUagtF0hTwPiWbQkoHEflnZBak4WTWnzoyMeqdn8+FPB+6Znqn9NWn63JfulqtUEI8H3GFIRqCYvM0l2lyIbtt5NQYGue4GjBLZnVUHT/pewDoK66RXm1UdMnL7oNNZN8+bPhl6bD1WxbgLvVMENnqCB1IhQxHmYRnSiscwY53lUqke0ZguH8JQxV5niSd5NCXrv3yH8hcGXQ9Yqu9PI0zpPRaBcSCaxMa3GcGFNSrvepPuWSJiXAUTnFYp1QQh9iclstPtPbk6e54BWBoljIkhcTZfD416k1RItCZ5vj+Mjm1t8KRk3/PVeB8GoaAUF6AIo7JbqswE4wDI+YIXrvUXP7/nSam2Ioak2SsU981qSEZNWdXl586CUXZJE+75JrJ6YpfYO8e12rAB0v0Xy0Ee/ddnqlk0E8zuLMNKpik4saHK7Y1CabVEagJ5KZqISOoyaDQ23yxgvpnt8D20Gd5SIo=; bm_sv=DE151528E8241821BC75A4AC0CF5533A~YAAQVG0/F8OR1cKFAQAAUYBR4xJcPXiDvJJWwW0p/aSrPsUKO1XLIzSCnSEamefUjiq4X5GCuslIZFfhJEww8nKoDzkRx81kjZv7Q7P3HFczZlk/LxLHaaimK++vFSCsmUJFADFlc1frmdWwjoWa+4rtkt4Ur9K2ofCfDlPeu6WWDpqJ3RaI1YII7sGPZKJ2kOiZHIE/G0pOc7BedGdx3WpdtnXJtiUKWGbSd56g+ZA//aR2mPODb/iw/c+d7SAeiQ==~1; _gat_UA-182658-1=1; HOWTORT=cl=1674556014512&r=https%3A%2F%2Fwww.naukri.com%2Fwordpress-jobs-3%3Fkk%3Dwordpress&nu=https%3A%2F%2Fwww.naukri.com%2Fwordpress-jobs-4',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

keyword = 'web-crawler'
alldata = []
def crwal_list():
    page =  1
    api = f'https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_keyword&searchType=adv&keyword={keyword}&pageNo={page}&sort=r&k={keyword}&seoKey={keyword}-jobs-{page}&src=jobsearchDesk&latLong='
    response = requests.get(api, headers=headers)
    js = response.json()
    total = js['noOfJobs']
    pages = total//20
#  403 not found
    for i in range(pages+1):
        api = f'https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_keyword&searchType=adv&keyword={keyword}&pageNo={page}&sort=r&k={keyword}&seoKey={keyword}-jobs-{page}&src=jobsearchDesk&latLong='
        response = requests.get(api, headers=headers)
        print(response.url,response)
        js = response.json()
        products = js.get('jobDetails')
        if products:
            for product in products:
                title = product.get('title')
                jobId = product.get('jobId')
                footerPlaceholderLabel = product.get('footerPlaceholderLabel')
                companyName = product.get('companyName')
                tagsAndSkills = product.get('tagsAndSkills')
                companyId = product.get('companyId')
                jdURL = 'https://www.naukri.com'+product.get('jdURL')
                jobDescription = bs(product.get('jobDescription')).text
                createdDate = product.get('createdDate')
                
                data = {
                    'title':title,
                    'jobId':jobId,
                    'footerPlaceholderLabel':footerPlaceholderLabel,
                    'companyId':companyId,
                    'companyName':companyName,
                    'tagsAndSkills':tagsAndSkills,
                    'jdURL':jdURL,
                    'jobDescription':jobDescription,
                    'createdDate':createdDate
                }
                print(data)
                alldata.append(data)
        page += 1
crwal_list()
df = pd.DataFrame(alldata)
df.to_excel('naukri.xlsx', index=False)

