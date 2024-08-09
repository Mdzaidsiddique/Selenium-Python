'''
headless mode: script execute in backend
- test execution is fast, performance increase
'''

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

def chrome_setup():
    driver = webdriver.Chrome()
    # ops = webdriver.ChromeOptions()
    # ops.headless = True
    return driver

driver = chrome_setup()

driver.get("https://www.apple.com/in/")
driver.maximize_window()
driver.implicitly_wait(10)

print(driver.title, driver.current_url)

driver.close()
