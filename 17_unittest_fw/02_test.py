import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# multiple test in one class
class SearchEngineTest(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        print(f"title of the page is : ", self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.bing.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        print(f"title of the page is : ", self.driver.title)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()



