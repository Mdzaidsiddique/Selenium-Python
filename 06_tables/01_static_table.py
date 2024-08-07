import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# count number of rows and columnscolumns = driver.find_element(By.XPATH, )
rows = driver.find_elements(By.XPATH, "//table[@Name= 'BookTable']//tr")
columns = driver.find_elements(By.XPATH, "//table[@Name= 'BookTable']//tr[1]/th")

print(f"rows: {len(rows)} and columns: {len(columns)}")

# Read specific row & column data
data = driver.find_element(By.XPATH, '//table[@Name= "BookTable"]//tr[5]/td[1]').text
print(data)

# Read all rows and columns data
for r in range(2, len(rows)+1):
    for c in range(1, len(columns)+1):
        # dynamic xPath : '+str(x)+'
        cell_data = driver.find_element(By.XPATH, '//table[@Name= "BookTable"]//tr['+str(r)+']/td['+str(c)+']').text
        print(cell_data)

# Read data based on condition
for r in range(2, len(rows)+1):
    auther_name = driver.find_element(By.XPATH, '//table[@Name= "BookTable"]//tr['+str(r)+']/td[2]').text
    if auther_name == "Mukesh":
        book_name = driver.find_element(By.XPATH, '//table[@Name= "BookTable"]//tr['+str(r)+']/td[1]').text
        print(book_name, ":", auther_name)


driver.close()