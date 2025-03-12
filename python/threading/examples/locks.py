from threading import Lock, RLock

def speak():
    print "Je suis libre"
    name = raw_input('c\'est quoi ton nom?')

if __name__ == '__main__':
    l = Lock()
    l.acquire()
    speak()
