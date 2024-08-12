 # explicit wait

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')

wait = WebDriverWait(driver, 10)
el = wait.until(expected_conditions.text_to_be_present_in_element((By.LINK_TEXT, 'Get the app')))
