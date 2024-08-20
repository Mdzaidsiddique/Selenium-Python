"""
# frames/iframes: webpage divided into multiple page, each divided section is called frames
if any elements are present inside frames we can not interact because frames are not web elements
we need to switch to particular frame
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/frames")
driver.get("https://www.selenium.dev/selenium/docs/api/java/deprecated-list.html")
driver.maximize_window()
driver.implicitly_wait(10)


# driver.switch_to.frame(frame name/ frame ID/ capture frame as web elements and pass / index (0,1,2,3..))

frame_element = driver.find_element(By.ID, "")
driver.switch_to.frame(frame_element)
# driver.find_elements().click()

# once our job is done to the first frame then we have to switch back to main frame, then we can switch to aother frmae

driver.switch_to.default_content() #back to main frame

# switch to the next frame
driver.switch_to.frame()
# perform action





