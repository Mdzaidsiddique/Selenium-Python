# stale Element Exception: cause: page refresh, navigate, DOM manipulation
import time

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
driver.maximize_window()

# 1st approach: relocate element again

# 2nd approach: try-catch
retries = 3
for i in range(retries):
    try:
        search_box = driver.find_element(By.CSS_SELECTOR, '#APjFqb')
        search_box.click()
        search_box.send_keys('welcome')
        search_box.send_keys(Keys.RETURN)
        break
    except StaleElementReferenceException:
        if i == retries - 1:
            continue
        else:
            raise


# 3rd approach: explicit wait

wait = WebDriverWait(driver, 3, poll_frequency=2, ignored_exceptions=[StaleElementReferenceException])

searchBox = wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#APjFqb')))
searchBox.click()
searchBox.send_keys("Welcome")
searchBox.send_keys(Keys.RETURN)

time.sleep(2)
driver.quit()