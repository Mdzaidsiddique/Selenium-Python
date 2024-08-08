import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()

# Css selectors:

# Tag and ID: tag_name#value_of_id, #id_value
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc@fb.com")

# Tag and Class: tag_name.value_of_class, .class_value
'''
sometimes in class/id/attribute if any space is there and after space the value is not taken so we have to remove that value
for example
class="zaid alif"
then take ".zaid" only
'''
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@facebook.com")

# Tag and attribute: tag[attribute = "value"]
driver.find_element(By.CSS_SELECTOR, "input[name = email]").send_keys("abc@facebook.com")

# Tag class and attribute: tag.class[attribute = value]
driver.find_element(By.CSS_SELECTOR, "input._6luy[name = pass]").send_keys("Abc#123")
time.sleep(2)




