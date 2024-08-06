import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# driver.implicitly_wait(10)

# select specific checkbox
driver.find_element(By.ID, "sunday").click() #check
driver.find_element(By.ID, "sunday").click() #uncheck
time.sleep(2)



checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")

print(len(checkboxes))

# select multiple checkboxes based on choice
for checkbox in checkboxes:
    days = checkbox.get_attribute('id')
    if days == "monday" or days == "fiday":
        checkbox.click()

# select last two checkboxes
for i in range(len(checkboxes)-2, len(checkboxes)):
    checkboxes[i].click()

# unselect checkbox
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

