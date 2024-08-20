# frame

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

frame_element = driver.find_element()
driver.switch_to.frame(frame_element)
driver.switch_to.parent_frame()
driver.switch_to.default_content()