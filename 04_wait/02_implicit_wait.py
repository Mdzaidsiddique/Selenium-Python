
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get("https://google.com")
driver.implicitly_wait(10) #applicable for all the below statements, untill quit() or close()
# default time is zero
# wait for element until element is not loaded, once element is available it will perform action
# single statement
# performance will not be reduced
# if element is not loaded until maximum defined time, then we can get exception
driver.maximize_window()

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
# search_box.send_keys(Keys.RETURN)
# or
search_box.submit()

driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()