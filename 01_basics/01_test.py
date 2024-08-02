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
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

assert "OrangeHRM" in driver.title

print(driver.title)