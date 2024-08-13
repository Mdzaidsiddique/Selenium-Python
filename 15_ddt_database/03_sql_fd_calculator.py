from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import mysql.connector
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
driver.implicitly_wait(10)

# data
try:
    con = mysql.connector.connect(host='localhost', user='root', passwd='root', database='mydb')
    cur = con.cursor()
    cur.execute('SELECT * FROM financial_records')

    for row in cur.fetchall():
        # storing data
        price = row[0]
        rate_of_interest = row[1]
        period1 = row[2]
        period2 = row[3]
        frequency = row[4]
        exp_maturity_value = row[5]

        print(price, rate_of_interest, period1, period2, frequency, exp_maturity_value)

        # passing data to application
        driver.find_element(By.XPATH, '//*[@id="principal"]').send_keys(price)
        driver.find_element(By.XPATH, '//*[@id="interest"]').send_keys(rate_of_interest)
        driver.find_element(By.XPATH, '//*[@id="tenure"]').send_keys(period1)

        print("35----------")
        period_dd = Select(driver.find_element(By.XPATH, '//*[@id="tenurePeriod"]'))
        period_dd.select_by_visible_text(period2)

        print("39----------")
        frequency_dd = Select(driver.find_element(By.XPATH, '//*[@id="frequency"]'))
        frequency_dd.select_by_visible_text(frequency)

        time.sleep(3)

        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()

        actual_maturity_value = driver.find_element(By.XPATH, "//span[@id = 'resp_matval']//strong").text

        # Validation
        if float(exp_maturity_value) == float(actual_maturity_value):
            print("Test Pass")
        else:
            print("Test Fail")

        # clear everything
        driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[2]/img').clear()

        time.sleep(3)

    con.close()
except:
    print("connection unsuccessful")


driver.close()
