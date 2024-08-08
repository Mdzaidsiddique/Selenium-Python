# ActionChains: Class to handle mouse operation in selenium
"""
mouse hover
double click
right click
drag and drop
slider
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# disable popup (page loading) #notification popups
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--disable-notifications')

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//*[@id='HTML4']/div[1]/button").click()

# switching browser windows
window_key = driver.window_handles
window_key_second = window_key[1]
print(window_key, window_key_second)
driver.switch_to.window(window_key_second)


desktop = driver.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[1]/a')
mac = driver.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[1]/div/div/ul/li[2]/a')

# ActionChain Class Object
act = ActionChains(driver)

# Hover action
act.move_to_element(desktop).move_to_element(mac).click().perform()

driver.switch_to.window(window_key[0])

driver.quit()

