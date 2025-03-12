import threading
import time

def worker():
    print threading.current_thread().getName(), 'Starting'
    print threading.current_thread().ident
    print threading.current_thread().name
    #print get_ident()
    print threading.current_thread().getName(), 'Exiting'

for i in xrange(5):
    t = threading.Thread(target=worker, name="mofo")
    t.start()
    print t.ident, 'again'

"""
- Thread.ident or Thread.get_ident() 
    - returns thread identifier or None if thread has not been started
    - nonzero integer
    - may be recycled when a thread exit and another is created.
    - available even after the thread has exited

- Thread.name, Thread.getName(), Thread.setName()
    - string used for identification
    - has no semantics
    - multiple threads may be given the same name
    - initial name is set by the constructor
"""
