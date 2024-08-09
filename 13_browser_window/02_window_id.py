import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)

# switch one window to another window
# switch_to.window(browser WindowID)
# window id: automatically generate when window open (Dynamic)

window_id = driver.current_window_handle #it will return window id of single browser window
print(window_id)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
time.sleep(2)

window_ids = driver.window_handles # this will return list (window ids) of multiple browser window
print(window_ids)

first_window = window_ids[0]
second_window = window_ids[1]

# switch window
driver.switch_to.window(second_window)
print(driver.title)

driver.switch_to.window(first_window)
print(driver.title)

# we can loop over multiple browser window
for win_id in window_ids:
    driver.switch_to.window(win_id)
    print(driver.title)

# close specefic browser windows based on choice
for win_id in window_ids:
    driver.switch_to.window(win_id)
    if driver.title != "OrangeHRM, Inc":
        driver.close()

time.sleep(3)

driver.quit()