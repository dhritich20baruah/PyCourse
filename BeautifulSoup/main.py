# Step 0: Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://dhritibaruah.in/articles/html-for-beginners-part-2"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)
# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)
# Step 3: HTML Tree traversal
title = soup.title
print(title)
# Commonly used types of objects
# 1. Tag 
# print(type(title))
# 2. NavigableString
# print(type(title.string))
# 3. BeautifulSoup
# print(type(soup))

paras = soup.find_all('p')
print(paras)

print(soup.find('h1'))