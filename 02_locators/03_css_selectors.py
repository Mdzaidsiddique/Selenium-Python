# Css selectors:
# Tag and ID: tag_name#value_of_id, #id_value
# Tag and Class: tag_name.value_of_class, .class_value
# Tag and attribute: tag[attribute = "value"]
# Tag class and attribute: tag.class[attribute = "
# xPath locators: absolute xPath and Relative xPath

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.cnn.com/")
driver.maximize_window()

# sometimes in class/id/attribute if any space is there and after space the value is not taken so we have to remove that value
# for example
# class="zaid alif"
# then take ".zaid" only