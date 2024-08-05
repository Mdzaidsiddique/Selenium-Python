# Application specefic command
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") #used to upen webpage
driver.maximize_window()

print(driver.title) #used to capture title of the current webpage
print(driver.current_url) #capture current url
print(driver.page_source) #cpature source code (html, css, js) of the page