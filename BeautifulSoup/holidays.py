from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "holiday"
file = 11
for country in ["wallis-and-futuna",
        "yemen",
        "zambia",
        "zimbabwe",
        "cook-islands"]:
    driver.get(f"https://www.timeanddate.com/holidays/{country}/2026")

    elems = driver.find_elements(By.CLASS_NAME, "table--holidaycountry")
    print(f"{len(elems)} items found")
    # print(elem.get_attribute("outerHTML"))

    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"holidays/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1
        # print(elem.text)
        
    time.sleep(2)

driver.close()