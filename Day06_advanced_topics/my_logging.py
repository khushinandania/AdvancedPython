import logging

logging.basicConfig(level = logging.WARNING,format = '%(asctime)s -%(name)s - %(levelname)s - %(message)s')

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)
logger_handler = logging.FileHandler('my_log.log')
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
logger_handler.setFormatter(formatter)
logger.addHandler(logger_handler)   

logger.debug("Debug message from my_logger")
logger.info("Info message from my_logger")
logger.warning("Warning message from my_logger")
logger.error("Error message from my_logger")
logger.critical("Critical message from my_logger")  


def divide(a , b):
    try:
        result = a / b
        logger.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError as e:
        logger.error("Attempted to divide by zero.")
        return None
    

divide(5, 2)
divide(10, 0)


