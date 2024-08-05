from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

# find_element(): return single web element
# 1) locator matching with single web element
element = driver.find_element(By.NAME, "email")

# 2) locator matching with mulitple web element, but if we use find_element() then first matching element will be captured

# 3) if the element is not found then NoSuchElementException


driver.find_element(By.NAME, "email").send_keys("<EMAIL>")


# find_elements(): captured multiple elements as List Collection, not raised any Exception
# if no element mathces then find_elements() will returned empty List
