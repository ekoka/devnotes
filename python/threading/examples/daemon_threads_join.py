import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)

def daemon():
    logging.debug('Starting')
    time.sleep(9)
    logging.debug('Exiting')

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

nd = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
nd.start()

d.join(4) # join with a 4 second timeout

print 'd.isAlive() ', d.isAlive()
