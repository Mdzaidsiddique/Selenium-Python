from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://bugbug.io/blog/testing-frameworks/best-selenium-practice-websites/")

driver.maximize_window() # maximize the window

# by class name
multiple_elements = driver.find_elements(By.CLASS_NAME, "MobileContentMenu_MobileContentMenu__menuListElement__tJqPg")

print(len(multiple_elements))

# by tag name
tag_name = driver.find_elements(By.TAG_NAME, value="a")
print(len(tag_name))