# Synchronization problem: sometimes browser takes time to load elements on webpages, if we try to access that elements
# before loaded then will get synchronization problem

# to overcome this problem we have three ways
# 1) time.sleep(t) : not really wait statement, it only pauses the code execution (from python not from webdriver)
#                  : even if element is present still it will wait t time to perform action
#                  : not recomonded: performace of the script is very poop
#                  : if element is not present within the t time, then we can get exception

# 2) implicit wait
# 3) explicit wait

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://google.com")
driver.maximize_window()

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
# search_box.send_keys(Keys.RETURN)
# or
search_box.submit()

driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()