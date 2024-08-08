# Application specefic command
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

# these commands we can access through web elements not through driver
# is_displayed() : check element is present or not : Returns True/False
search_box = driver.find_element(By.NAME, "q")
print(search_box.is_displayed()) #True

# is enabled()   : Returns True/False
print(search_box.is_enabled()) #True

# is_selected()  : radio buttons and checkboxes : Returns True/False
radio_button_male = driver.find_element(By.XPATH, '//*[@id="gender-male"]')
radio_button_female = driver.find_element(By.XPATH, '//*[@id="gender-female"]')
radio_button_female.click() #select radio button

print("male: ", radio_button_male.is_selected())
print(f"Female: {radio_button_female.is_selected()}")