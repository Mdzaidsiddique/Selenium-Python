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


"""
*) universal selector: select all elements in a document
tagName : tag name
.className : class selector
#idSelecotor : id selector
[type='submit'] : attribute selector
div p : ancestor descendant
ul > li : parent > child
h1 + p : adjusent + sibling (h1 + p selects the first <p> element immediately following any <h1> element)
h1 ~ p : General Sibling Selector (h1 ~ p selects all <p> elements that are siblings of any <h1> element)
"""
