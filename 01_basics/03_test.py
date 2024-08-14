import time
import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.google.co.in/")

# element = driver.find_element(*(By.XPATH, "//textarea[@id='APjFqb']"))
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@id='APjFqb']"))).send_keys("ind vs sl live")

# element.send_keys("ind vs sl live")
# element.send_keys(Keys.ENTER)

time.sleep(10)





