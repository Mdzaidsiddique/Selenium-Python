"""
Logging:
Logging is a very useful tools in a programmers toolbox,
It can help you develop better understanding of the flow of hte program and discover scenario that you might
not have thought of while developing

Log Level:
Debug, Info, Warning, Error, Critical
"""
import logging

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename=r'C:\Users\mdzaids\Desktop\Selenium-Python\16_logging\01_test.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logging.debug('This is a debug message')
logging.info('This is an info message')

logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')



