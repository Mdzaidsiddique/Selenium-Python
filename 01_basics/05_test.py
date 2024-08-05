
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?returnUrl=%2F")

driver.maximize_window()

email_box = driver.find_element(By.ID, "Email")
email_box.clear()
email_box.send_keys("abc@gmail.com")

print(email_box.text) #text will always return Inner Text of the element: <div>Inner Text</div>

# .get_attribute(attribute) #return value of any attribute value of a web element
print(email_box.get_attribute("value"))
print(email_box.get_attribute("id"))



