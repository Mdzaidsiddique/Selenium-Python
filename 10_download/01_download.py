import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import os

# download fine scenario will different from browser to browser specially in firefox

driver = webdriver.Chrome()
driver.get("https://mdzaidsiddique.github.io/")
driver.maximize_window()
driver.implicitly_wait(10)

# download at default location
driver.find_element(By.XPATH,'//*[@id="resume-link-1"]').click()

driver.close()