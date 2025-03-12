'''
- using a daemon thread can be useful for services where there may not be an easy way to interrupt the thread or where letting the thread die in the middle of its work does not lose or corrupt data (e.g. a thread that generates "heart beats").
- to mark a thread as daemon call its `setDaemon()` method with a boolean argument, thread are not daemon by default.
'''

import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)

def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

nd = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
nd.start()

'''
- if you run this script as main, the output won't include the Exiting message from the daemon thread, since all the non-daemon thread (including the main thread) exit before the daemon thread wakes up from its 2 second sleep.
- if on the other hand you import it from a running shell (the main thread in this instance) the daemon thread's output will show.

- to wait until a daemon thread has completed its task use the join() method.
    >>> d.join()

- by default join() blocks indefinitely, you can pass a timeout argument

    >>> d.join(5) # wait 5 seconds

'''
