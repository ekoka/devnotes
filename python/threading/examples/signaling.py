'''
- at times you may want to communicate between threads. a simple way to this using `threading.Event` objects.
- `Event` manages an internal flag that caller can `set()` or `clear()`, other threads `wait()` for the flag to be `set()`, effectively blocking progress until allowed to continue.
- a thread can pass a timeout argument to `Event.wait()`, if Event hasn't been `set()` sometimes within that timeframe the calling thread unblocks (resumes processing).
'''
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)-10s %(message)s'
)


def worker(e):
    '''wait for the event to be set before doing anything'''
    logging.debug('worker starting')
    logging.debug('worker waiting for event')
    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)

def worker_with_timeout(e, t):
    '''wait t seconds and then timeout'''
    logging.debug('worker_with_timeout starting')
    while not e.isSet():
        logging.debug('worker_with_timeout waiting for event %s seconds', t)
        event_is_set = e.wait(t)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')

e = threading.Event()

t1 = threading.Thread(
    name='block',
    target=worker,
    args=(e,))
t1.start()

t2 = threading.Thread(
    name='non-block',
    target=worker_with_timeout,
    args=(e, 4))
t2.start()

timeout = 20
logging.debug('waiting %s seconds before calling Event.set()', timeout)
time.sleep(timeout)
e.set()
logging.debug('Event is now set')
