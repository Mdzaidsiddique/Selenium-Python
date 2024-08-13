import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

logger.basicConfig(filename='02_test_logger.log', filemode='w', level=logging.DEBUG)