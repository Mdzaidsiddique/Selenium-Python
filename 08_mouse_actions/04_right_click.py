
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
driver.implicitly_wait(10)

element = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/p/span")


action_chains = ActionChains(driver)
action_chains.context_click(element).perform()

driver.quit()