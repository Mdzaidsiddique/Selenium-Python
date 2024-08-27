
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import openpyxl
import time
import excel_utils

driver = webdriver.Chrome()

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")

driver.maximize_window()

file = r"C:\Users\mdzaids\Desktop\Selenium-Python\14_data_driven_testing\03_fd_calculator.xlsx"

rows = excel_utils.get_row_ount(file, "data")
columns = excel_utils.get_column_ount(file, "data")

for row in range(2, rows+1):
    price = excel_utils.read_data(file, "data", row, 1)
    rate_of_interest = excel_utils.read_data(file, "data", row, 2)
    period1 = excel_utils.read_data(file, "data", row, 3)
    period2 = excel_utils.read_data(file, "data", row, 4)
    frequency = excel_utils.read_data(file, "data", row, 5)
    exp_maturity_value = excel_utils.read_data(file, "data", row, 6)

    # Passing data to the application
    driver.find_element(By.ID, "principal").send_keys(price)
    driver.find_element(By.ID, "interest").send_keys(rate_of_interest)
    driver.find_element(By.XPATH, '//*[@id="tenure"]').send_keys(period1)


    period_dd = Select(driver.find_element(By.XPATH, '//*[@id="tenurePeriod"]'))
    period_dd.select_by_visible_text(period2)

    frequency_dd = Select(driver.find_element(By.XPATH, '//*[@id="frequency"]'))
    frequency_dd.select_by_visible_text(frequency)

    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()

    actual_maturity_value = driver.find_element(By.XPATH, "//span[@id = 'resp_matval']//strong").text

    # Validation
    if float(exp_maturity_value) == float(actual_maturity_value):
        print("Test Pass")
        excel_utils.write_excel(file, "data", row, 8, "Passed")
        # apply color
        excel_utils.fill_green_colour(file, "data", row, 8)
    else:
        print("Test Fail")
        excel_utils.fill_red_colour(file, "data", row, 8)

    # clear everything
    driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[2]/img').clear()

    time.sleep(3)
    
driver.quit()