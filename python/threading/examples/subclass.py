'''
- at start-up a Thread does some basic initialization and then calls its run() method, which calls the target function passed to the constructor

- when subclassing Thread override run() in consequence.

'''
import threading
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)-10s %(message)s',
)

class MyThread(threading.Thread):
    def run(self):
        logging.debug('running')


for i in range(5):
    t = MyThread()
    t.start()
'''
- `args` and `kwargs` passed to Thread.__init__() are saved in private variables, to access them from a subclass, redefine __init__() to save arguments in attributes that are visible in the subclass.
'''

class MyThreadWithArgs(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target, name=name,
                                  verbose=verbose)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug('running')


for i in range(5):
    t = MyThreadWithArgs(args=(i,), kwargs={'a':'A', 'b':'B'})
    t.start()
