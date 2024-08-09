import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import os

def chrome_set_up():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(os.getcwd() + r"\sample_download.pdf")
    chrome_prefs = {
        "download.default_directory": os.getcwd(),      # Set the download directory
        "download.prompt_for_download": False,          # Don't prompt for download
        "download.directory_upgrade": True,             # Allow directory upgrade
        "safebrowsing.enabled": True                    # Enable safe browsing
    }

    chrome_options.add_experimental_option("prefs", chrome_prefs)

    driver = webdriver.Chrome(options=chrome_options)
    return driver

driver = chrome_set_up()
driver.get("https://mdzaidsiddique.github.io/")

driver.find_element(By.XPATH,'//*[@id="resume-link-1"]').click()

driver.close()











# download_path = '/path/to/your/download/directory'
#
# # Set up Chrome options
# chrome_options = Options()
# chrome_prefs = {
#     "download.default_directory": download_path,  # Set the download directory
#     "download.prompt_for_download": False,         # Don't prompt for download
#     "download.directory_upgrade": True,            # Allow directory upgrade
#     "safebrowsing.enabled": True                    # Enable safe browsing
# }
# chrome_options.add_experimental_option("prefs", chrome_prefs)
#
# # Initialize the Chrome WebDriver
# driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=chrome_options)