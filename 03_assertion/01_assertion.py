from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://google.com")

assert "Google" in driver.title

print(driver.title)