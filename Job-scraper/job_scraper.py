from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "job"

driver.get(f"https://www.assamcareer.com/2022/12/ahidms-recruitment.html")

elems = driver.find_elements(By.ID, "PostBody")
print(f"{len(elems)} items found")
# print(elem.get_attribute("outerHTML"))

for elem in elems:
    d = elem.get_attribute("outerHTML")
    with open(f"job/{query}.html", "w", encoding="utf-8") as f:
        f.write(d)
    # print(elem.text)
    
time.sleep(2)

driver.close()