import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch Chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()

@when('open Orange HRM home page')
def open_home_page(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    context.driver.maximize_window()

@then('verify that the logo present on page')
def verify_logo(context):
    status = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[1]/img').is_displayed()
    assert status is True
    time.sleep(2)

@then('cloe browser')
def close_browser(context):
    context.driver.close()