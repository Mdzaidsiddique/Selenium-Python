# browser ---> application

# close(): close the application but broswer specific process won't be killed and close one browser (tab) at a time
# quit(): close the broswer along with the process, and close all the browser(tab)

from selenium import webdriver
from selenium.webdriver.common.by import By

# launch browser
driver = webdriver.Chrome()

# open a website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()
# driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a").click()

driver.close()

driver.quit()
