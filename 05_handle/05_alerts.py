# alerts are also called pop-ups
# switch to alerts

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[1]/button").click()

# alert windows are not a web element, driver will not be about to interact

time.sleep(2)

alert_window = driver.switch_to.alert

alert_window.text
print(alert_window.text)

# alert_window.send_keys("welcome") #type something in alert window if it is prompt alert

# close alert window by OK button
alert_window.accept()

# close alert window by cancel button
# alert_window.dismiss()

driver.quit()

"""
authenticated alerts: while launching page alert came and ask login credentials (browser authentication)
because alerts are not page elements so we can not provide value by send_keys()
here we use concept of injection
# injection syntax: https://username:password@abc.com
"""

driver = webdriver.Chrome()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
