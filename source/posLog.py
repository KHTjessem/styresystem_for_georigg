import threading
import time


class posLogger(threading.Thread):
    def __init__(self, cont_ref, waitTime):
        threading.Thread.__init__(self)
        self.__cont = cont_ref
        
        self.newRunEV = threading.Event()
        self.ev = threading.Event()
        self.posData = posData()
        self.ent = posDataEnt # Reference to class

        self.__startTime = None
        self.waitTime = waitTime
    

    def run(self):
        while True:
            print("ready to log")
            self.newRunEV.wait()
            print("Stated logging position")
            self.newRun()
            self.work()
            self.newRunEV.clear()
    
    def work(self):
        while self.newRunEV.is_set():
            pos = self.__cont.getActualPosition()
            t = self.__startTime - time.time()
            self.posData.newEntry(self.ent(pos, t))
            print(f"newpos: {pos}, at {t} s")
            time.sleep(self.waitTime)


    
    def newRun(self):
        self.posData.newRun()
        self.__startTime = time.time()


    def stop(self):
        self.newRunEV.clear()

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
        print(ent)
        self.__data[self.__currentRun].append(ent)
        self.lock.release()

    def newRun(self):
        self.lock.acquire()
        self.__data.append([])
        self.__currentRun += 1
        self.lock.release()
    
    def getAllData(self):
        self.lock.acquire()
        k = self.__data
        print(k)
        self.lock.release()
        return k
    
    def getLatestData(self):
        self.lock.acquire()
        d = self.__data[self.__currentRun]
        self.lock.release()
        return d

from dataclasses import dataclass

@dataclass
class posDataEnt:
    pos: int
    sec: int

