# http://stackoverflow.com/questions/104983/what-is-thread-local-storage-in-python-and-why-do-i-need-it

from time import sleep
from random import random
from threading import Thread, local
from thread import get_ident

data = local()

def bar():
    print "I'm called from", data.v
    print "and my id is: ", get_ident()
    print "and my id is: ", get_ident()
    print "and my id is: ", get_ident()
    print "and my id is: ", get_ident()
    print "and my id is: ", get_ident()

def foo():
    print "my id is: ", get_ident()
    print "my id is: ", get_ident()
    print "my id is: ", get_ident()
    try:
        bar()
    except AttributeError:
        pass


class T(Thread):
    def run(self):
        sleep(random())
        data.v = self.getName()
        sleep(1)
        #bar()
        foo()

foo()

T().start()
T().start()
T().start()
T().start()


