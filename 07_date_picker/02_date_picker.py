# DOB Picker

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.ID, "dob").click()

select_month = Select(driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']/Select[1]"))
select_month.select_by_visible_text("Jul")

# Select Object
select_year = Select(driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']/Select[2]"))
select_year.select_by_visible_text("1999")

dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in dates:
    if int(date.text) == 10:
        date.click()
        break

driver.close()

