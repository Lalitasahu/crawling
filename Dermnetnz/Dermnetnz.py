import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import Session
s=Session()

xl=csv.writer(open('Disesas.csv','w',newline=''))
xl.writerow(['Name','Dease_URL','Dease_image'])

cookies = {
    'CountryCode': 'IND',
    '_ga_ZVT7LBZQ5J': 'GS1.1.1671264730.3.1.1671267220.0.0.0',
    '_ga': 'GA1.2.1721434919.1671212181',
    '_gid': 'GA1.2.140479744.1671212182',
    'ln_or': 'eyIzNTg5MTY0IjoiZCJ9',
    'fs.session.id': '90be45fb-78d9-4a15-ad17-e59adb9cde53',
    '__qca': 'P0-1004165285-1671212182679',
    '_jsuid': '556460815',
    '__gads': 'ID=ee65aac2b1e9e9da-22466c74ecd800ac:T=1671212312:S=ALNI_MZHZvpDceTuty35DFF2BKEInCrtrQ',
    '__gpi': 'UID=00000b91fdbbd5ed:T=1671212312:RT=1671245870:S=ALNI_MboHQmDg4nsBjPSHttrNQ89KPCosA',
    '_awl': '2.1671267228.5-e561585545de29b2d83052f208d587e7-6763652d617369612d6561737431-0',
    '_pbjs_userid_consent_data': '3524755945110770',
    'cookie': 'ccdf8507-f514-484a-9b5d-a154bb0d47b8',
    '_lr_env_src_ats': 'false',
    'cto_bundle': 'lQzLOF92TlBMYkQySVB5SHZDSlpVdEpHJTJCTHREZkJXaFpCSiUyRnVZSjB6c3RKZVduYnVOUTFVN1ZwenE5NWNUa1VIWDJrVjBGVDNXRjlNUTFneURKSzdncFpVN0UyVzFnMGlPcjBsb0hOVEdhUXAySzZUYnF3ZzF2WGJDeXA1YyUyQkFOQWhPTEZoRkRRSmVTOGI4M1JwbXRhYSUyRlkyQSUzRCUzRA',
    'cto_bidid': 'ep1Yo19oR2ZPdHY0cmpPczdIMEMyN0J6YW9nOVgyQ0pIR0VpM3NlcDJkbWpmWGo4aUxqU0JuOWxoZVhXS1pIQUJkQVEwSE1ZZ3VDdGpBJTJCa3lYYmdkYkk4a1djemxyJTJGNm9zQXE5S1JsZjEwdmxWNDAlM0Q',
    'cnx_userId': '97df7b10dc7c45199b945fef76ec2ae2',
    '_au_1d': 'AU1D-0100-001671212193-87R22OML-H4TE',
    '_au_last_seen_pixels': 'eyJhcG4iOjE2NzEyMTIxOTMsInR0ZCI6MTY3MTIxMjE5MywicHViIjoxNjcxMjEyMTkzLCJ0YXBhZCI6MTY3MTIxMjE5MywiYWR4IjoxNjcxMjEyMTkzLCJnb28iOjE2NzEyMTIxOTMsImltcHIiOjE2NzEyMTIxOTMsIm1lZGlhbWF0aCI6MTY3MTIxMjE5MywidW5ydWx5IjoxNjcxMjEyMTkzLCJydWIiOjE2NzEyMTIxOTN9',
    '_au_last_seen_iab_tcf': '1671212194011',
    '_fbp': 'fb.1.1671212195997.91076322',
    'cto_dna_bundle': '6NzjpF80M0RITmhlJTJCZkMwOUJGQlhaMUN2c3picGNhMTQxNnFsVUt5SlBJN3hHU09SMzMyWm9kJTJCZCUyRk53bzFCa2JuS1B5',
    '_pk_id.1090.e4ed': 'e6d25a8806a85ddc.1671212393.',
    'PHPSESSID': 'k56mqbui0l987tf0s08sder0s7',
    'fs.bot.check': 'true',
    '_bannerAds': 'eyJzbG90cyI6WzM5LDQxLDQzXX0=',
    '_pk_ses.1090.e4ed': '1',
    'dmd-ahk': '5125f93b1a',
    'dmd-signal-246-10250-3F3B6BD6-34846446-ed8e-4579-80b7-e0a3c3ac512e': 'e30=',
    '_lr_retry_request': 'true',
    '_sess': '7b4d8d73-3467-44a7-b07d-27b7cb771444.f43e15ef-efe1-4e01-993b-92c5f640cabc.1671267099.1',
    'dmd-vid': 'f43e15ef-efe1-4e01-993b-92c5f640cabc',
    'dmd-sid': '7b4d8d73-3467-44a7-b07d-27b7cb771444',
    '_heatmaps_g2g_101371808': 'no',
    'dmd-signal-246-10250-3F3B6BD6-7b4d8d73-3467-44a7-b07d-27b7cb771444': 'e30=',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://dermnetnz.org/image-library',
    # 'Cookie': 'CountryCode=IND; _ga_ZVT7LBZQ5J=GS1.1.1671264730.3.1.1671267220.0.0.0; _ga=GA1.2.1721434919.1671212181; _gid=GA1.2.140479744.1671212182; ln_or=eyIzNTg5MTY0IjoiZCJ9; fs.session.id=90be45fb-78d9-4a15-ad17-e59adb9cde53; __qca=P0-1004165285-1671212182679; _jsuid=556460815; __gads=ID=ee65aac2b1e9e9da-22466c74ecd800ac:T=1671212312:S=ALNI_MZHZvpDceTuty35DFF2BKEInCrtrQ; __gpi=UID=00000b91fdbbd5ed:T=1671212312:RT=1671245870:S=ALNI_MboHQmDg4nsBjPSHttrNQ89KPCosA; _awl=2.1671267228.5-e561585545de29b2d83052f208d587e7-6763652d617369612d6561737431-0; _pbjs_userid_consent_data=3524755945110770; cookie=ccdf8507-f514-484a-9b5d-a154bb0d47b8; _lr_env_src_ats=false; cto_bundle=lQzLOF92TlBMYkQySVB5SHZDSlpVdEpHJTJCTHREZkJXaFpCSiUyRnVZSjB6c3RKZVduYnVOUTFVN1ZwenE5NWNUa1VIWDJrVjBGVDNXRjlNUTFneURKSzdncFpVN0UyVzFnMGlPcjBsb0hOVEdhUXAySzZUYnF3ZzF2WGJDeXA1YyUyQkFOQWhPTEZoRkRRSmVTOGI4M1JwbXRhYSUyRlkyQSUzRCUzRA; cto_bidid=ep1Yo19oR2ZPdHY0cmpPczdIMEMyN0J6YW9nOVgyQ0pIR0VpM3NlcDJkbWpmWGo4aUxqU0JuOWxoZVhXS1pIQUJkQVEwSE1ZZ3VDdGpBJTJCa3lYYmdkYkk4a1djemxyJTJGNm9zQXE5S1JsZjEwdmxWNDAlM0Q; cnx_userId=97df7b10dc7c45199b945fef76ec2ae2; _au_1d=AU1D-0100-001671212193-87R22OML-H4TE; _au_last_seen_pixels=eyJhcG4iOjE2NzEyMTIxOTMsInR0ZCI6MTY3MTIxMjE5MywicHViIjoxNjcxMjEyMTkzLCJ0YXBhZCI6MTY3MTIxMjE5MywiYWR4IjoxNjcxMjEyMTkzLCJnb28iOjE2NzEyMTIxOTMsImltcHIiOjE2NzEyMTIxOTMsIm1lZGlhbWF0aCI6MTY3MTIxMjE5MywidW5ydWx5IjoxNjcxMjEyMTkzLCJydWIiOjE2NzEyMTIxOTN9; _au_last_seen_iab_tcf=1671212194011; _fbp=fb.1.1671212195997.91076322; cto_dna_bundle=6NzjpF80M0RITmhlJTJCZkMwOUJGQlhaMUN2c3picGNhMTQxNnFsVUt5SlBJN3hHU09SMzMyWm9kJTJCZCUyRk53bzFCa2JuS1B5; _pk_id.1090.e4ed=e6d25a8806a85ddc.1671212393.; PHPSESSID=k56mqbui0l987tf0s08sder0s7; fs.bot.check=true; _bannerAds=eyJzbG90cyI6WzM5LDQxLDQzXX0=; _pk_ses.1090.e4ed=1; dmd-ahk=5125f93b1a; dmd-signal-246-10250-3F3B6BD6-34846446-ed8e-4579-80b7-e0a3c3ac512e=e30=; _lr_retry_request=true; _sess=7b4d8d73-3467-44a7-b07d-27b7cb771444.f43e15ef-efe1-4e01-993b-92c5f640cabc.1671267099.1; dmd-vid=f43e15ef-efe1-4e01-993b-92c5f640cabc; dmd-sid=7b4d8d73-3467-44a7-b07d-27b7cb771444; _heatmaps_g2g_101371808=no; dmd-signal-246-10250-3F3B6BD6-7b4d8d73-3467-44a7-b07d-27b7cb771444=e30=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailersip',
}

allData = []
url = 'https://dermnetnz.org/topics/acne-affecting-the-back-images?stage=Live'
def Diseasepage():
    response = requests.get('https://dermnetnz.org/image-library/imagesJson', cookies=cookies, headers=headers)
    js = response.json()
    for diseas in js:
        Name = diseas.get('page_name')
        Dease_URL = 'https://dermnetnz.org'+diseas.get('url')
        Dease_image =diseas.get('thumbnail')
        
        data ={
            'Name':Name,
            'Dease_URL':Dease_URL,
            'Dease_image':Dease_image
        }

        xl.writerow(data.values())
        allData.append(data)
        print(allData)

Diseasepage()
df = pd.DataFrame(allData)
df.to_excel('Deases.xlsx', index=False)


