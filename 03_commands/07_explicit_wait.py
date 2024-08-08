from selenium.common import ElementNotInteractableException, ElementNotSelectableException, ElementNotVisibleException, \
    NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()

# Explicit wait works based on the condition not based on time
# my_wait = WebDriverWait(driver, 10) # explicit wait declaration
# here 10 is the cut off time, in line 22 if element is nto present then condition will not true, and untill method will keeep on waiting
# to exit from that situation we provide cutoff time, to execute next statements

my_wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                        ElementNotInteractableException, ElementNotVisibleException,
                                                        ElementNotSelectableException, Exception])
# even explicit wait raise Exception then Exception handle automatically in upper my_wait obj

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()

# driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()
# find_element() is inclusive in explicit wait
search_link = my_wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
search_link.click()

driver.quit()

# Advantage:
# 1) Most Effectively works
# 2) No need to use find_elements()



