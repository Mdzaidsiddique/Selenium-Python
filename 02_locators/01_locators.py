import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.python.org")

# x-Path: locators
# search_box = driver.find_element(By.XPATH, "//input[@id = 'id-search-field']")

# Name
search_box = driver.find_element(By.NAME, "q")

# CSS Selector
search_box = driver.find_element(By.CSS_SELECTOR, "input[name='q']")
elements = driver.find_elements(By.CSS_SELECTOR, "input[name='q']")

# Tag Name or Class Name: to find more than one element
search_box = driver.find_element(By.TAG_NAME, "input")

element_by_class = driver.find_elements(By.CLASS_NAME, value="header-banner ")

# linked test and partila linked text
# about = driver.find_element(By.LINK_TEXT, u"About" ).click()

# about = driver.find_element(By.PARTIAL_LINK_TEXT, "out").click()
time.sleep(3)

# search_box.send_keys("python")
# search_box.send_keys(Keys.ENTER)

driver.close() # close one browser
driver.quit() # close all the browsers


