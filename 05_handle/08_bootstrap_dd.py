import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(10)

# drop down without select tag

driver.find_element(By.ID, "select2-billing_country-container").click()

country_list = driver.find_elements(By.XPATH, "//ul[@id = 'select2-billing_country-results']/li")

for country in country_list:
    if country.text == 'India':
        country.click()
        break

time.sleep(4)

driver.close()