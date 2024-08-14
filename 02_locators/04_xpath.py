""" 
xPath: it is defined as XML path
It is the syntax or language for finding any web elements by using XML path expression
Find location of any web element by using HTML DOM Structure
Can be used to navigate through elements and attribute in DOM
xPath is the address of the element

Types of xPath
1) absolute (full) xPath: start from root node
                    /html/body/div/div[1]/div/div[1]/div/div[1]/img

2) Relative (partial) xPath: start from immidiate parent node
                    //*[@id="app"]/div[1]/div/div[1]/div/div[1]/img

inspect--> right click on html tag-->copy-->copy xpath
SelectorHub extension
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()

# absolute xPath:
# driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys("abc@fb.com")

# relative xPath: //tagname[@attribue = value], //*tagname[@attribute = value]
# driver.find_element(By.XPATH, "//*[@id='pass']").send_keys("12345")

# or: //tagname[attribute1 = value or attribute2 = value]
# driver.find_element(By.XPATH, "//*[@value='1' or @normalize-space='Log In'] ").click()

# and: just like or we can go with and operator

# [contains(@attribute,'some chars of id')]
driver.find_element(By.XPATH, "//*[contains(@id,'email')]")

# [start-with(@attribute, 'strating chars')]
driver.find_element(By.XPATH, "//*[starts-with(@aria-label, 'Pass') ]")

# text() : //*a[text()='Log In']

time.sleep(2)

"""
Prefer relative Xpath over abs xpath, because
- if developers intoduce new element then abs xPath will be broken
- If Location of element will changed then abs xpath will be broken
absolute xPath is unstable
"""