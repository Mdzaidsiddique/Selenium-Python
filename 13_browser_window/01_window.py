from selenium.webdriver.chrome import webdriver

driver = webdriver.Chrome()

# lauch 2 app in new window, and switch to that page
driver.get("https://www.apple.com/in/")

driver.switch_to.new_window("tab") #open new tab
driver.switch_to.new_window('window') # open in new browser window

driver.get("https://www.google.com/")

driver.close()