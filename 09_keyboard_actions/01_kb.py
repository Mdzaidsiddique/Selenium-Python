# ActionChains Class

import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://text-compare.com/")
driver.maximize_window()
driver.implicitly_wait(10)

input_area1 = driver.find_element(By.ID, "inputText1")
input_area1.send_keys("Welcome to textarea 1...")


action_chain = ActionChains(driver)

# Cntr+A
action_chain.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

# Cntr+C
action_chain.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# Press tab key to navigate to input 2 box
action_chain.send_keys(Keys.TAB).perform()

# input_area2 = driver.find_element(By.XPATH, "//textarea[@Id = 'inputText2']")
# dont required really because tab key switch to this input area

# Contr+v
action_chain.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

time.sleep(4)

driver.close()


# tab -->move to next field

# Contr+V

