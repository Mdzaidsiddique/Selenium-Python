# Test Case
# 1) Open web browser(Chrome/firefox/Edge)
# 2) Open Url (https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)
# 3) Enter username: Admin
# 4) Enter Password: admin123
# 5) Click on login
# 6) Capture title
# 7) varify title
# 8) close browser

# webdriver is a module which is available in selenium package
from selenium import webdriver
from selenium.webdriver.common.by import By

# launch browser
driver = webdriver.Chrome()

# open a website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Locate an input field and enter text
username = driver.find_element(*(By.CSS_SELECTOR, "input[placeholder='Username']"))
password = driver.find_element(*(By.CSS_SELECTOR, "input[placeholder='Password']"))

username.clear()
username.send_keys("Admin")
password.clear()
password.send_keys("admin123")

# find_element(): find all the matching elements and go with the first one
# find_elements(): find all the matching elements
login = driver.find_element(*(By.CSS_SELECTOR, "button[type='submit']"))
login.click()

actual_title = driver.title
expected_title = 'OrangeHRM Live'

if actual_title == expected_title:
    print("Login successful and test case got passed")
else:
    print("Login failed and test case got failed")

# close a browser
driver.close() # close one browser
driver.quit() # close all the browsers


