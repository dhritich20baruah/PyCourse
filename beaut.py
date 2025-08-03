import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

print(soup)