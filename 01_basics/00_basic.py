# install selenium: pip install selenium

# pip show selenium
# uninstall selenium: pip uninstall selenium

import selenium

print(selenium.__version__)

# selenium archetecture
"""
Java, Python, C#, Ruby
       |
JSON Wire Protocol: This was the original protocol used by Selenium to communicate between the client library and the browser drivers. It sends HTTP requests in JSON format to perform actions in the browser.
W3C WebDriver Protocol: This is the newer, standardized protocol that Selenium 4 and above use to interact with browsers. It ensures better compatibility and standardization across different browsers.
       |
Web drivers
       |
Web browsers    

"""