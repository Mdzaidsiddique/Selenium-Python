import os
import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.apple.com/in/")
driver.maximize_window()
driver.implicitly_wait(10)

# path = "C:\\Users\\mdzaids\\Desktop\\Selenium-Python\\12_miscellaneous\\homepage.png" # doubling \\
# path = r"C:\Users\mdzaids\Desktop\Selenium-Python\12_miscellaneous\homepage.png" #raw string

# driver.save_screenshot(r"C:\Users\mdzaids\Desktop\Selenium-Python\12_miscellaneous\homepage.png")

driver.save_screenshot(os.getcwd()+"\homepage1.png")

# driver.get_screenshot_as_file()
# driver.get_screenshot_as_base64() or # driver.get_screenshot_as_png() # it will save ss as binary

driver.close()