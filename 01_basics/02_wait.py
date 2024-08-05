# To handle dynamic content, use waits. There are two types: implicit and explicit waits.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

chrome_driver = webdriver.Chrome()
edge_driver = webdriver.Edge()

chrome_driver.get('https://google.com')

title = chrome_driver.title
print(title)

# Implicit Wait: Wait up to n seconds for elements to appear
chrome_driver.implicitly_wait(5)

assert 'Google' in chrome_driver.title

# explicit wait
try:
    element = WebDriverWait(chrome_driver, 10).until(
        lambda x: x.find_element_by_tag_name('h1')
    )
    element.send_keys('Google')
finally:
    chrome_driver.quit()


