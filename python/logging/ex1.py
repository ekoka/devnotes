# simple logger
import logging

logging.basicConfig(filename="outputs/ex1.log", level=logging.DEBUG,
                    filemode="w")
#logging.basicConfig(filename="outputs/ex1.log", level=logging.INFO,
#                    filemode="w")

logging.info('info message')
logging.error('error message')
# debug will only be logged at level=logging.DEBUG
logging.debug('this is a debug message') 

