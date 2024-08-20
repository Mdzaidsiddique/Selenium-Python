# <400: Responce Code (Normal links)
# >400: Error Code (broken list)
import requests
# Pre-Req: install requests module: setting->python interpreter-> add requests module and install package


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME, "a")

count = 0

for link in all_links:
    url = link.get_attribute('href')
    # url will not open but requests module send request to server and get response object
    # to avoid network exception surround with try catch
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url, ": is broken list")
        count += 1
    else:
        print(url, ": is valid link")

print(f"Total number of broken links: {count}")


