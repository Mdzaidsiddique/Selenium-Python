from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
driver.maximize_window()
driver.implicitly_wait(10)

wait = WebDriverWait(driver, 10, 2, ignored_exceptions=[StaleElementReferenceException])
search_box= wait.until(expected_conditions.presence_of_element_located((By.NAME, "q")))
search_box.clear()
search_box.send_keys("python")
search_box.send_keys(Keys.RETURN)

driver.close()