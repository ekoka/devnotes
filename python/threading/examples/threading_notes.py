"""
`threading` module
------------------
- builds on the low-level features of `threads` module
- easier, more pythonic way to work with threads

Thread object
-------------
- simplest way to use a Thread is to instantiate it with a target function an call its `start()` method
"""

import threading
from thread import get_ident 

def worker(num):
    """thread worker function"""
    print 'Worker: ', num
    print get_ident()
    return

threads = []

for i in xrange(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

