# At the VERY TOP of EVERY .py file
import logging

logging.basicConfig(level=logging.DEBUG, filemode='w', filename='example.log', format='%(asctime)s-%(levelname)s:%(message)s')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
