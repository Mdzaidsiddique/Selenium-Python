import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://practice.expandtesting.com/upload")
driver.maximize_window()
driver.implicitly_wait(5)

upload = driver.find_element(By.ID, 'fileInput')
upload.send_keys(r"C:\Users\mdzaids\Desktop\Selenium-Python\11_upload\xpath pdf.pdf")

time.sleep(2)

driver.close()

"""
(type attribute should be 'file' in case of input tag, otherwise with js
execute script need to add the set attribute type as file)
"""