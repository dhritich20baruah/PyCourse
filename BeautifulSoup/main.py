# Step 0: Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "http://localhost:8020/blogs/63554d6241dbdf1f5c7b0a0f"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)
# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)
# Step 3: HTML Tree traversal
title = soup.title
print(title)