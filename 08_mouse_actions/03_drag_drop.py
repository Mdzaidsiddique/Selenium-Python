import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

source = driver.find_element(By.XPATH, '//*[@id="draggable"]')
target = driver.find_element(By.XPATH, '//*[@id="droppable"]')

action_chain = ActionChains(driver)
action_chain.drag_and_drop(source, target).perform()

driver.quit()