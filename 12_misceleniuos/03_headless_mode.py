'''
headless mode: script execute in backend
- test execution is fast, performance increase
'''

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.apple.com/in/")
driver.maximize_window()
driver.implicitly_wait(10)

print(driver.title, driver.current_url)

driver.close()
