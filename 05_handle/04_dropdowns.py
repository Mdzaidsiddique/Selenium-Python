import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# DropDowns: <Select> and <option> Tag
dd_country_element = driver.find_element(By.ID, "country")

dd_country = Select(dd_country_element) #this obj will be use to select option form dd

# select option from dd
# dd_country.select_by_visible_text("India")
# time.sleep(1)
# dd_country.select_by_value("uk")
# time.sleep(1)
# dd_country.select_by_index(2)

# capture all the options

all_options = dd_country.options
print(len(all_options))

for option in all_options:
    print(option.text)

# select option from dd without using built-in methods
for option in all_options:
    if option.text == 'USA':
        option.click()
        break
