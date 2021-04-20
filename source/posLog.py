import threading
import time


class posLogger(threading.Thread):
    def __init__(self, conn_ref, comData, waitTime, gap):
        threading.Thread.__init__(self)
        self.__conn = conn_ref
        self.comData = comData
        
        self.gapCom = gap
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
            t = self.__startTime - time.time()
            pos = self.getPos()
            self.posData.newEntry(self.ent(pos, t))
            print(f"newpos: {pos}, at {t} s")
            time.sleep(self.waitTime)

    def getPos(self):
        self.__conn.tlock.acquire()
        self.comData.newCommand(self.gapCom)
        self.__conn.newComEv.set()
        self.__conn.replyReadyEv.wait()
        pos = self.comData.getReply()
        self.__conn.replyReadyEv.clear()
        self.__conn.tlock.release()
        return pos.value

    
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
        
        self.__currentRun = -1
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
        pos = [None]*len(d)
        sec = [None]*len(d)
        
        indx = 0
        for x in d:
            pos[indx] = x.pos
            sec[indx] = x.sec
            indx += 1
            
        self.lock.release()
        return [sec, pos]

from dataclasses import dataclass

@dataclass
class posDataEnt:
    pos: int
    sec: int

