import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
time.sleep(2)
driver.get("https://www.google.com")
driver.maximize_window()


driver.back()
driver.forward()
driver.refresh()

driver.close()
driver.quit()