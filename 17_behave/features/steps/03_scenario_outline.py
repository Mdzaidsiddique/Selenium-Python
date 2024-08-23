from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'I Launch Chrome browser')
def step1_impl(context):
    context.driver = webdriver.Chrome()


@when(u'I Open orange HRM homepage')
def step2_impl(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when(u'Enter username "{user}" and password "{pwd}"')
def step3_impl(context, user, pwd):
    context.driver.find_element(By.NAME, 'username').send_keys(user)
    context.driver.find_element(By.NAME, 'password').send_keys(pwd)

@when(u'Click on login button')
def step4_impl(context):
    context.driver.find_element(By.XPATH, "//button[text()=' Login ']").click()

@then(u'User must successfully login to dashboard page')
def step5_impl(context):
    # context.driver.find_element(By.XPATH, "//div[@id='app']//h6[text()='Dashboard']")
    try:
        assert context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[1]/a/div[2]/img').is_displayed()
    except:
        assert False, "Test Failed"

    context.driver.close()



