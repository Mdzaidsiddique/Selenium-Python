# Action class will not support in scrolling
# we can hanlde page scrolling with javascript
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
driver.maximize_window()
driver.implicitly_wait(10)

# 1) scroll down by page pixel
driver.execute_script("window.scrollBy(0, 3000)", "")
moved_pixel = driver.execute_script("return window.pageYOffset;")

print(moved_pixel) #3000

# 2) scroll down till element is visible
# india_flag = driver.find_elements(By.CSS_SELECTOR, "img[src='/img/flags/small/tn_in-flag.gif']")

# driver.execute_script("arguments[0].scrollIntoView();", india_flag)
# moved_pixel = driver.execute_script("return window.pageYOffset;")

# print(moved_pixel)

# 3) scroll till end
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

# 4) scroll up
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight);")


time.sleep(5)
driver.close()