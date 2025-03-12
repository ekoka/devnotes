'''
- python's built-in data structures (list, dict, tuple, set) are thread-safe because the GIL is not released while manipulating them. 
- simpler types such as int and floats don't have that protection
- other data structures implemented in python might also not be thread-safe
- to prevent corruption or missed data when accessing shared resources use `threading.Lock()` objects
'''

import threading
import random
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)-10s %(message)s'
)

class Counter(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.counter1 = self.counter2 = start

    def increment_without_lock(self):
        self.counter1 = self.counter1 + 1

    def increment_with_lock(self):
        #logging.debug('waiting for lock')
        self.lock.acquire()
        try:
            #logging.debug('acquired Lock')
            self.counter2 = self.counter2 + 1
        finally:
            #logging.debug('releasing Lock')
            self.lock.release()

def worker(c):
    for i in range(50000):
        c.increment_without_lock()
        c.increment_with_lock()

counter = Counter()
for i in range(5):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

logging.debug('waiting for worker threads')
main_thread = threading.currentThread()

for t in threading.enumerate():
    if t is not main_thread:
        t.join()

logging.debug('Counter1: %d', counter.counter1)
logging.debug('Counter2: %d', counter.counter2)
