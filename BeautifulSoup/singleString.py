from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
for i in range(1, 20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&xpid=pSgy7HC4v6kp5&crid=2QJUXBH5B3J1V&qid=1754576531&sprefix=laptop%2Caps%2C348&ref=sr_pg_2")

    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")
    # print(elem.get_attribute("outerHTML"))

    for elem in elems:
        print(elem.text)
        
    time.sleep(2)
    driver.close()