import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.flipkart.com/")

action_chain = ActionChains(driver)

driver.find_element(By.XPATH, "//span[text()='Electronics']").click()


audio = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/object/a[1]")
soundbar = driver.find_element(By.XPATH, "//a[text()='Soundbars']")

action_chain.move_to_element(audio).move_to_element(soundbar).click().perform()


driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div[2]').click()

time.sleep(2)

product = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/a[2]').text

price = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/a[3]/div[1]/div[1]').text
print(price)

# product.__getattribute__("title")
time.sleep(3)

driver.close()


