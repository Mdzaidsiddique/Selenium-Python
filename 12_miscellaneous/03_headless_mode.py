'''
headless mode: script execute in backend
- test execution is fast, performance increase
'''

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.apple.com/in/")
driver.maximize_window()
driver.implicitly_wait(10)

print(driver.title, driver.current_url)

driver.close()
