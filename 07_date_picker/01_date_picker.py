
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame(0) #there is only one frame, 0th index point to that frame

# mm/dd/yyyy
# driver.find_element(By.ID, "datepicker").send_keys("08/08/2024")

year = "2025"
month = "March"
day = "08"

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

while True:
    mm = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yyyy = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if yyyy == year and mm == month:
        break
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click() #next arrow
        # driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click() #prev arrow

# date picker
dates = driver.find_elements(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')

for d in dates:
    if int(d.text) == int(day):
        d.click()
        break

driver.quit()

