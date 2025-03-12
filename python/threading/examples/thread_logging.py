import logging
import threading
import time

"""
- you can include the name of the current thread in the log's debug output by using the formater code %(threadName)s
"""
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s'
    )

def worker():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def my_service():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exiting')

w = threading.Thread(name='worker', target=worker)
s = threading.Thread(name='service', target=my_service)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
s.start()
