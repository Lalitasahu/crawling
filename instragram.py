import requests

cookies = {
    'csrftoken': 'bvxFmQjNRyKX5sUpZ3G5ENwnLOamfKDH',
    'mid': 'ZABuSQAEAAEBJh2qXQ6E53z5YB7u',
    'ig_did': '6AE179FD-E613-4717-A762-AABBBA38A483',
    'ig_nrcb': '1',
    'datr': 'Qm4AZOyjAXWD-zyBNnaE1UfS',
    'ds_user_id': '53068359800',
    'sessionid': '53068359800%3AMhKfE165Shp2DL%3A11%3AAYfwP3uKDr5KMqllkOFpFF0qWPLezuhjBm53NPRE4g',
    'shbid': '"7860\\05453068359800\\0541711255352:01f77b5b66ea05353b1d87817393ea13d7c19466fccdb3031315bba7ec757f00eaed2c14"',
    'shbts': '"1679719352\\05453068359800\\0541711255352:01f7472b3123e0303a32977837f5bb92697c23dc9537e0fd0dcf4c528a71ac91f209e500"',
    'dpr': '2',
    'rur': '"EAG\\05453068359800\\0541711292674:01f74ae52f75a98d944702b39c9256c4aace679626e7f8d05d7941557ea6fccb33c44fd6"',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': 'bvxFmQjNRyKX5sUpZ3G5ENwnLOamfKDH',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '198387',
    'X-IG-WWW-Claim': 'hmac.AR0Tt0tRSnW1rG28sCck5Q3veBvryL4rHFPDjjGXmGOkXQot',
    'X-Requested-With': 'XMLHttpRequest',
    'Alt-Used': 'www.instagram.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/cristiano/',
    # 'Cookie': 'csrftoken=bvxFmQjNRyKX5sUpZ3G5ENwnLOamfKDH; mid=ZABuSQAEAAEBJh2qXQ6E53z5YB7u; ig_did=6AE179FD-E613-4717-A762-AABBBA38A483; ig_nrcb=1; datr=Qm4AZOyjAXWD-zyBNnaE1UfS; ds_user_id=53068359800; sessionid=53068359800%3AMhKfE165Shp2DL%3A11%3AAYfwP3uKDr5KMqllkOFpFF0qWPLezuhjBm53NPRE4g; shbid="7860\\05453068359800\\0541711255352:01f77b5b66ea05353b1d87817393ea13d7c19466fccdb3031315bba7ec757f00eaed2c14"; shbts="1679719352\\05453068359800\\0541711255352:01f7472b3123e0303a32977837f5bb92697c23dc9537e0fd0dcf4c528a71ac91f209e500"; dpr=2; rur="EAG\\05453068359800\\0541711292674:01f74ae52f75a98d944702b39c9256c4aace679626e7f8d05d7941557ea6fccb33c44fd6"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'count': '12',
    'max_id': '3037988821844906714_173560420',
}

response = requests.get('https://www.instagram.com/api/v1/feed/user/173560420/', params=params, cookies=cookies, headers=headers)

js = response.json()
