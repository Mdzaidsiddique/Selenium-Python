import time

'''
cookies: temprary file created by the browser
'''

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.apple.com/in/")
driver.maximize_window()
driver.implicitly_wait(10)

# capture cookies from browser, cookies are having number of attributes
cookies = driver.get_cookies()

print(len(cookies))

# print details of all cookies
for c in cookies:
    # print(c)
    print(c.get('name'), ":", c.get('value'))

# add new cookie to the browser
driver.add_cookie({"name":"my_cookie", "value":"my_value"})

cookies = driver.get_cookies() # again need to capture all the cookies

print(f"after adding new cookies: {len(cookies)}")

# Delete specific cookie from browser by name
driver.delete_cookie("my_cookie")
cookies = driver.get_cookies() # again need to capture all the cookies
print(f"after detetioon {len(cookies)}")


# Delete all the cookie from browser
driver.delete_all_cookies()
cookies = driver.get_cookies() # again need to capture all the cookies
print(f"after deteting of all cookies : {len(cookies)}")

time.sleep(2)
driver.close()
