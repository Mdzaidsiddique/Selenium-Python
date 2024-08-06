# links
# 1) internal link: after clicking open on same page
# 2) external link: open on other page
# 3) broken link: link without target page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click() #sometime partial value ,match with some other element

# find total number of links in a page
links = driver.find_elements(By.TAG_NAME, "a")
xlinks = driver.find_elements(By.XPATH, "//a")

print(f"Total number of links: {len(links)} and {len(xlinks)}")

for link in links:
    print(link.text)