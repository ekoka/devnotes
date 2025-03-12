from time import sleep
from random import random
from threading import Thread

def bar():
    global v
    print "I'm called from", v

def foo():
    bar()


class T(Thread):
    def run(self):
        global v
        sleep(random())
        v = self.getName()
        sleep(1)
        foo()
        #bar()

T().start()
T().start()
T().start()
T().start()


