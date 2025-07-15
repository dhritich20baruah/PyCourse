import requests
import time
from fake_useragent import UserAgent
url = "https://www.flipkart.com/search?q=hard+disk+1tb&sid=6bo%2Cjdy&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=hard+disk+1tb%7CStorage&requestId=4f6f986f-1378-46f6-b01e-e2b1ee9a90a7&as-searchtext=hard%20disk%201tb"

url2 = "https://webscraper.io/test-sites/e-commerce/allinone"

session = requests.Session()

headers = {
    'User-Agent': UserAgent().random,
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.google.com'
}

proxy_auth = ''

proxies = {
    'http': f'http://{proxy_auth}',
    'https': f'http://{proxy_auth}'
}

time.sleep(2)
r = session.get(url2)
# print(r.text)

with open("file.html", "w") as f:
    f.write(r.text)