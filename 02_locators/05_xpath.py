
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# self
element = driver.find_element(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr[6]/td[1]/a/self::a").text

print(element) #Dr. Lal Pathlabs Ltd


# parent:  /parent::tagname
#/ancestor::
#/child::
# /decendant::* (all the decendant node)
# /following::*, following-siblng::* -->above self
# /preceding::*, /preceding-sibling::* -->below self