import threading
import time

class posLogger(threading.Thread):
    def __init__(self, ):
        threading.Thread.__init__(self)
        self.__cont = con_ref
        
        self.ev = threading.Event()
        self.posData = posData()

        self.__startTime = None
    

    def run(self):
        while True:
            self.ev.wait() # wait for engine to start


    
    def newRun(self):
        self.posData.newRun()
        self.__startTime = time.time
        self.ev.set()

    def stop(self):
        self.ev.clear()

# TODO: Check if actually need lock.
# Might only need to access data when engine is not running,
# so no new data being added while retrieving
class posData:
    def __init__(self):
        self.lock = threading.Lock()
        
        self.__currentRun = 0
        self.__data = []

    def newEntry(self, ent):
        self.lock.acquire()
        self.__data[self.__currentRun].append(ent)
        self.lock.release()

    def newRun(self):
        self.lock.acquire()
        self.__data.append([])
        self.__currentRun += 1
        self.lock.release()
    
    def getData(self):
        self.lock.acquire()
        k = self.__data
        self.lock.release()
        return k
    