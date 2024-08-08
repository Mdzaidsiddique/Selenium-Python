from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

slider_rail = driver.find_element(By.ID, 'slider')
slider_button = driver.find_element(By.XPATH, '//*[@id="slider"]/span')

print(slider_button.location)

action_chain = ActionChains(driver)
action_chain.drag_and_drop_by_offset(slider_button, 100, 0).perform()

print(slider_button.location)

driver.close()