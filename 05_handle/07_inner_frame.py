# inner frame: a frame contains another frame

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/frames")
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()

driver.switch_to.frame((driver.find_element(By.XPATH, "//*[@id='Multiple']/iframe")))

inner_iframe = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(inner_iframe)

driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("Welcome")

time.sleep(2)

# inner to frame frame:

driver.switch_to.parent_frame() #outer iFrame( immediate parent frame)
