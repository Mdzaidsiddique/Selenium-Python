import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

double_click_button = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')

action_chain = ActionChains(driver)
action_chain.double_click(double_click_button).perform()

driver.close()