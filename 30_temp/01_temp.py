# stale element reference exception, how to handle it(try-except)

## Exceptions in selenium
# NoSuchElementException
# NoSuchFrameException
# NoSuchWindowException
# NoAlertPresentException
# ElementNotVisibleException
# ElementNotInteractableException
# StaleElementReferenceException
# TimeoutException
# InvalidArgumentException

# implicit wait throws: NoSuchElements
# explicit wait throws: timeOutException

"""
order(based on performance): id, name, className, CSSSelector, xPath, tagName, linkedText, PartialLinedText

locators practice ... very imp, dynamic elements (amazon, flipkart)

# cotains()
# xPath axes: child-to parent

waits: explicit -> WebDriverWait(driver, timeout, ignoreException)
                   .untill(EC.presence_of_element_located(By.XPATH, locator))

tab and window switching: driver.switch_to_window('tab')
                          driver.switch_to.window('window')
                          driver.window_handles
                          driver.current_window_handle

frames switching: driver.switch_to.frame(frame_element)
                  driver.switch_to.parent_frame()
                  driver.switch_to.default_content()

alert handling: al = driver.switch_to.alert
                al.accept()
                al.dismiss()
                driver.ger(https://username:passwrd@abc.com) #for auth alerts

select class: (s= Select(e)
             s.options will return list,
             1:s.select_by_vt("x")
             2: s.select_by_value("y"),
             3: by_index(1)

actionChains (ac = ActionChains(driver)), .methods .perform

page Refresh:  (driver.back(), forward(), refresh(),
                actionChain (control+r),
                execute-script('history.go[0]):


how to upload a file using selenium (type attribute should be 'file' in case of input tag, otherwise with js
execute script need to add the set attribute type as file)
"""

# problem with selenium RC and grid
# how to create a grid