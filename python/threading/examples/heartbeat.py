import threading
import time

class Heartbeat(object):
    stop = False

    def __init__(self, interval=5):
        self.interval = interval

    def daemon(self):
        while not self.stop:
            self.tic()
            time.sleep(self.interval)

    def tic(self):
        print 'tic'

heartbeat = Heartbeat()
t = threading.Thread(target=heartbeat.daemon)
t.start()

key = None
while not key=='s':
    key = raw_input('press "s" to stop')

heartbeat.stop = True

