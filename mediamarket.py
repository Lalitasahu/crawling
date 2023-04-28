import requests
import json
from lxml import html
from requests import Session
s = Session

import requests

cookies = {
    'optid': 'cbe3a83a-69a6-4f14-8eff-cf3140a71f8b',
    'a': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiI1MGM4MDdiNi0yMTc0LTQ3NDctYTg1YS04ZjAwNmMzMTQ5YTUiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjgxMjI3MjEwLCJleHAiOjE2ODI0MzY4MTAsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTEyNX0.QPOmmqEmMd2wmv_exzbufJ1r3raZ4-IoXSi6IxsecC2gyvkrgp2_4PFV2h1z75v2omE8IMd1sGg8NJmUnV2N436otwJ_SNP0dgMk28KZT-yJO3-ZvhmUf1h0HStj-6gGEu6C-2eu0Z491OMn4M1xqfjWf7-RI049Yb_tx5QxpmmxXdLmFTk11uXZW9lCBUru8UFf25agTfCYsgAiS_TtJR62eC8WWArmUYiaPtRBPcLT0ajzmVQIDD9Oq5J5_56GABnYp_PQa1zyEG84vCT_aWeGhszvciarQxndafDFuoOyKhea72QFSaK9aEu7cBpOc-qeAZbja1g3AM6P_-LJcQ',
    'r': 'ge+V3Gpu7YvbJg0DA+NmzSCjs2PmY5UEMFOcRox9V1EPegxF3U3CrMeLdd8oxtU6',
    'pwaconsent': 'v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,con:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lib:1,lob:1,opt:1,orc:1,ore:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&cri:1,eam:1,fab:1,fbc:1,fcm:1,gac:1,gad:1,gcl:1,gcm:1,gdv:1,gos:1,gse:1,msb:1,omp:1,pin:1,ttd:1,twt:1|',
    '_gcl_au': '1.1.1456156908.1681227219',
    '_ga': 'GA1.2.50c97cbf-ca69-4b41-8ded-23815dd33e0c',
    '_cs_c': '1',
    '_cs_id': 'ccc8d449-598e-a7d5-e8e0-c4da310ad455.1681227219.5.1681310639.1681310632.1.1715391219198',
    '_ga_WK3CRFV96J': 'GS1.1.1681310641.3.0.1681310641.60.0.0',
    '_pin_unauth': 'dWlkPU1EZGhPVGhrTVRrdE4ySXlZUzAwTjJZM0xXRXdOV0V0WkdVNFpEZGxNVFZqTXpGaw',
    '_gid': 'GA1.2.647777372.1681227220',
    '_fpid': '50c97cbf-ca69-4b41-8ded-23815dd33e0c',
    '_fbp': 'fb.1.1681227221385.719777606',
    'BVBRANDID': '15fa950f-bfcc-404b-898f-14c552597709',
    'cto_bundle': 'QSXrS19UdnVaNFhtYTJvcmdRbDV6dFh6U1RwN2xjU1RKUmZiOW9mZklXV2FndyUyRm1JOHZHbFFUWHNhMFVaVXBISkRyQnhSUjc1UGN4RSUyQlNnNHVXYU4zMThnY2NsZE5ZakZqd0hBb0VsdFFTdTZza0tHUm9VdldrJTJGUFF4UFlZTHoyNlclMkZXSzFNbjdMOXlreEFoUFkyMnhCWk54JTJGNDlmJTJCJTJGOFh5aEtvRmN1RnBlbEFNNzE5SU1HekdiSFlhJTJGT1ZjS0glMkI2dVM',
    '__cf_bm': 'gRsZeBsmK8ct90SEXvkURjSvb8ZMoDWIL0peL_6ZkNE-1681310627-0-AS858UITP6H3D05BaH0D6LDjNHOoN7FlcTeyhOQlXLzbfGoXXSzDxMyT3r4Fxcnau5rG8psK9PRtVwBwGMlp7aigOpxdyngPMC//iv8UWv5I',
    '_cfuvid': 'qmXKO5swqzxfjsYOfX_dHbhH4IKh4bLHkHePNQcqt60-1681310627418-0-604800000',
    'ts_id': '9ae1d553-b8cb-484e-9165-8e15bd24e227',
    't_fpd': 'true',
    '_msbps': '99',
    '__cfruid': 'f654a64a9e7240f1ffdeeab99cb48906e232c0ed-1681310629',
    's_id': '536208c7-5f7c-4378-bdfa-47eb5e6ee46c',
    'MC_PS_SESSION_ID': '536208c7-5f7c-4378-bdfa-47eb5e6ee46c',
    'p_id': '536208c7-5f7c-4378-bdfa-47eb5e6ee46c',
    'MC_PS_USER_ID': '536208c7-5f7c-4378-bdfa-47eb5e6ee46c',
    'lux_uid': '168131063163408728',
    '_cs_s': '2.0.0.1681312439842',
    '_dc_gtm_UA-36693629-1': '1',
    '_uetsid': '3b68b460d87e11ed92a1d57034cec5dc',
    '_uetvid': '3b68c340d87e11edbdac5f317be14b2f',
    '_clck': 'qojp3x|1|fap|0',
    '_clsk': '1hi8olc|1681310645607|1|1|x.clarity.ms/collect',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.mediamarkt.de/de/category/notebooks-362.html?page=2',
    'content-type': 'application/json',
    'apollographql-client-name': 'pwa-client',
    'apollographql-client-version': '7.126.0',
    'x-operation': 'CategoryV4',
    'x-flow-id': 'df7a0fc4-940d-4e4b-aac4-06bef18b6983',
    'x-cacheable': 'true',
    'x-mms-language': 'de',
    'x-mms-country': 'DE',
    'x-mms-salesline': 'Media',
    'Connection': 'keep-alive',
    # 'Cookie': 'optid=cbe3a83a-69a6-4f14-8eff-cf3140a71f8b; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiI1MGM4MDdiNi0yMTc0LTQ3NDctYTg1YS04ZjAwNmMzMTQ5YTUiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjgxMjI3MjEwLCJleHAiOjE2ODI0MzY4MTAsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTEyNX0.QPOmmqEmMd2wmv_exzbufJ1r3raZ4-IoXSi6IxsecC2gyvkrgp2_4PFV2h1z75v2omE8IMd1sGg8NJmUnV2N436otwJ_SNP0dgMk28KZT-yJO3-ZvhmUf1h0HStj-6gGEu6C-2eu0Z491OMn4M1xqfjWf7-RI049Yb_tx5QxpmmxXdLmFTk11uXZW9lCBUru8UFf25agTfCYsgAiS_TtJR62eC8WWArmUYiaPtRBPcLT0ajzmVQIDD9Oq5J5_56GABnYp_PQa1zyEG84vCT_aWeGhszvciarQxndafDFuoOyKhea72QFSaK9aEu7cBpOc-qeAZbja1g3AM6P_-LJcQ; r=ge+V3Gpu7YvbJg0DA+NmzSCjs2PmY5UEMFOcRox9V1EPegxF3U3CrMeLdd8oxtU6; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,con:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lib:1,lob:1,opt:1,orc:1,ore:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&cri:1,eam:1,fab:1,fbc:1,fcm:1,gac:1,gad:1,gcl:1,gcm:1,gdv:1,gos:1,gse:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.1456156908.1681227219; _ga=GA1.2.50c97cbf-ca69-4b41-8ded-23815dd33e0c; _cs_c=1; _cs_id=ccc8d449-598e-a7d5-e8e0-c4da310ad455.1681227219.5.1681310639.1681310632.1.1715391219198; _ga_WK3CRFV96J=GS1.1.1681310641.3.0.1681310641.60.0.0; _pin_unauth=dWlkPU1EZGhPVGhrTVRrdE4ySXlZUzAwTjJZM0xXRXdOV0V0WkdVNFpEZGxNVFZqTXpGaw; _gid=GA1.2.647777372.1681227220; _fpid=50c97cbf-ca69-4b41-8ded-23815dd33e0c; _fbp=fb.1.1681227221385.719777606; BVBRANDID=15fa950f-bfcc-404b-898f-14c552597709; cto_bundle=QSXrS19UdnVaNFhtYTJvcmdRbDV6dFh6U1RwN2xjU1RKUmZiOW9mZklXV2FndyUyRm1JOHZHbFFUWHNhMFVaVXBISkRyQnhSUjc1UGN4RSUyQlNnNHVXYU4zMThnY2NsZE5ZakZqd0hBb0VsdFFTdTZza0tHUm9VdldrJTJGUFF4UFlZTHoyNlclMkZXSzFNbjdMOXlreEFoUFkyMnhCWk54JTJGNDlmJTJCJTJGOFh5aEtvRmN1RnBlbEFNNzE5SU1HekdiSFlhJTJGT1ZjS0glMkI2dVM; __cf_bm=gRsZeBsmK8ct90SEXvkURjSvb8ZMoDWIL0peL_6ZkNE-1681310627-0-AS858UITP6H3D05BaH0D6LDjNHOoN7FlcTeyhOQlXLzbfGoXXSzDxMyT3r4Fxcnau5rG8psK9PRtVwBwGMlp7aigOpxdyngPMC//iv8UWv5I; _cfuvid=qmXKO5swqzxfjsYOfX_dHbhH4IKh4bLHkHePNQcqt60-1681310627418-0-604800000; ts_id=9ae1d553-b8cb-484e-9165-8e15bd24e227; t_fpd=true; _msbps=99; __cfruid=f654a64a9e7240f1ffdeeab99cb48906e232c0ed-1681310629; s_id=536208c7-5f7c-4378-bdfa-47eb5e6ee46c; MC_PS_SESSION_ID=536208c7-5f7c-4378-bdfa-47eb5e6ee46c; p_id=536208c7-5f7c-4378-bdfa-47eb5e6ee46c; MC_PS_USER_ID=536208c7-5f7c-4378-bdfa-47eb5e6ee46c; lux_uid=168131063163408728; _cs_s=2.0.0.1681312439842; _dc_gtm_UA-36693629-1=1; _uetsid=3b68b460d87e11ed92a1d57034cec5dc; _uetvid=3b68c340d87e11edbdac5f317be14b2f; _clck=qojp3x|1|fap|0; _clsk=1hi8olc|1681310645607|1|1|x.clarity.ms/collect',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'operationName': 'CategoryV4',
    'variables': '{"hasMarketplace":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"isTeaserV3Active":false,"filters":[],"pimCode":"CAT_DE_MM_362","page":2,"experiment":"mp"}',
    'extensions': '{"persistedQuery":{"version":1,"sha256Hash":"e09611e5e408150be73bf010a2de0b4d40bb8e11dea4cb02a27af1d0dcdb94a0"},"pwa":{"salesLine":"Media","country":"DE","language":"de","globalLoyaltyProgram":true,"fifaUserCreation":true}}',
}

response = requests.get('https://www.mediamarkt.de/api/v1/graphql', params=params, cookies=cookies, headers=headers)
print(response)

# def listpage():
#     response = requests.get('https://www.mediamarkt.de/api/v1/graphql',
#                             params=params, headers=headers)
#     print(response)
#     # js = json.loads(response.json())
#     # products = js['data']['categoryV4']['products']
#     # for product in products:
#     #     Title = product.get('productAggregate').get('product').get('title')
#     #     print(Title)


# listpage()
