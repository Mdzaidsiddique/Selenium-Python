import time
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument('--disable-notifications')

driver = webdriver.Chrome()

driver.get("https://whatmylocation.com/#google_vignette")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.LINK_TEXT, 'Latitude and Longitude').click()

driver.find_element(By.XPATH, "//*[@id='utm_latitude_inp']").send_keys("123")
time.sleep(2)