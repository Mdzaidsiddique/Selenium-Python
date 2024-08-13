import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://practice.expandtesting.com/upload")
driver.maximize_window()
driver.implicitly_wait(10)

upload = driver.find_element(By.XPATH, '//*[@id="fileInput"]')
upload.click()
upload.send_keys(r"D:\file\kartik _resume (1)")

time.sleep(2)

driver.close()
