import requests 
import re
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import session
s = session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
params = {
    'passkey': 'b5sbvchuo8alfvu32evh0bnug',
    'apiversion': '5.5',
    'displaycode': '19244-en_us',
    'resource.q0': 'products',
    'filter.q0': 'id:eq:26167829',
    'stats.q0': 'reviews',
    'filteredstats.q0': 'reviews',
    'filter_reviews.q0': 'contentlocale:eq:en_EU,en_US',
    'filter_reviewcomments.q0': 'contentlocale:eq:en_EU,en_US',
    'resource.q1': 'reviews',
    'filter.q1': [
        'isratingsonly:eq:false',
        'productid:eq:26167829',
        'contentlocale:eq:en_EU,en_US',
    ],
    'sort.q1': 'submissiontime:desc',
    'stats.q1': 'reviews',
    'filteredstats.q1': 'reviews',
    'include.q1': 'authors,products,comments',
    'filter_reviews.q1': 'contentlocale:eq:en_EU,en_US',
    'filter_reviewcomments.q1': 'contentlocale:eq:en_EU,en_US',
    'filter_comments.q1': 'contentlocale:eq:en_EU,en_US',
    'limit.q1': '8',
    'offset.q1': '0',
    'limit_comments.q1': '3',
    'callback': 'BV._internal.dataHandler0',
}
allreview = []
def review(url):
    url = row['pro_URL']
    a = url.split('/')[-1]
    params['filter.q0'] = 'id:eq:'+ a
    params['filter.q1'] = ['productid:eq:'+a]
    response = requests.get('https://api.bazaarvoice.com/data/batch.json', params=params)
    
    name = re.findall('"UserNickname":"(.*?)",',response.text)
    title = re.findall('"Title":"(.*?)",',response.text)
    nick_name = re.findall('"UserNickname":"(.*?)",',response.text)
    comment = re.findall('"ReviewText":"(.*?)",',response.text)
    deta = re.findall('"SubmissionTime":"(.*?)",',response.text) 
    for n, t, s, c, d, in zip(name,title,nick_name,comment, deta):
        data = {
            'landingUrl':row['pro_URL'],
            'name':n,
            'title':t,
            'nick_name':s,
            'comment':c,
            'deta':d
        }
        allreview.append(data)
        print(data)

df = pd.read_excel('Clarksusa.xlsx')
for u in range(len(df)):
    row = df.iloc[u].to_dict()
    review(row)
url = 'https://www.clarksusa.com/c/Kaylin-Cara-2/p/26154701'
# url = 'https://www.clarksusa.com/c/Clarkwell-Demi/p/26167535'
# review(url)
df = pd.DataFrame(allreview)
df.to_excel('susa_reviews.xlsx', index=False)



