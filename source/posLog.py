import threading
import time


class posLogger(threading.Thread):
    def __init__(self, conn_ref, comData, waitTime, gap, events, maxtime=0):
        threading.Thread.__init__(self)
        self.__conn = conn_ref
        self.comData = comData
        self.evs = events
        
        self.gapCom = gap
        self.newRunEV = threading.Event()
        self.ev = threading.Event()
        self.posData = posData()
        self.ent = posDataEnt # Reference to class

        self.__startTime = None
        self.totTime = 0
        self.maxTime = maxtime
        self.waitTime = waitTime

        self.prevPos = None
    

    def run(self):
        """Main running loop of thread"""
        while True:
            print("ready to log")
            self.newRunEV.wait()
            print("Stated logging position")
            self.newRun()
            self.work()
            self.newRunEV.clear()
    
    def work(self):
        """Threads main workload"""
        while self.newRunEV.is_set():
            t = time.time() - self.__startTime
            pos = self.getPos()
            self.posData.newEntry(self.ent(pos, t))
            if pos is not None:
                self.evs.evs.updatePosition(pos/10240) # 10240 microsteps = 1 mm displacement
            if pos == self.prevPos:
                self.newRunEV.clear()
                self.evs.evs.updStatus(3)
            else:
                self.prevPos = pos
            time.sleep(self.waitTime)

    def getPos(self):
        """Gets the position of the enigne in microsteps"""
        self.__conn.tlock.acquire()
        self.comData.newCommand(self.gapCom)
        self.__conn.newComEv.set()
        self.__conn.replyReadyEv.wait()
        pos = self.comData.getReply()
        self.__conn.replyReadyEv.clear()
        self.__conn.tlock.release()
        if isinstance(pos, str):
            return None
        return pos.value

    
    def newRun(self):
        """Start from 0 again"""
        self.posData.newRun()
        self.__startTime = time.time()


    def stop(self):
        """Stops the main loop"""
        self.newRunEV.clear()


# TODO: Maybe store position log in a csv file.
class posData:
    """A class for keeping track of engines position"""
    def __init__(self):
        self.lock = threading.Lock()
        
        self.__currentRun = -1
        self.__data = []

    def newEntry(self, ent):
        """Adds a new position entry to self.currentRun index of list"""
        self.lock.acquire()
        #print(ent)
        self.__data[self.__currentRun].append(ent)
        self.lock.release()

    def newRun(self):
        """New run entry in list"""
        self.lock.acquire()
        self.__data.append([])
        self.__currentRun += 1
        self.lock.release()
    
    def getAllData(self):
        """Returns all runs position data"""
        self.lock.acquire()
        k = self.__data
        #print(k)
        self.lock.release()
        return k
    
    def getLatestData(self):
        """Get latest runs position data"""
        self.lock.acquire()
        d = self.__data[self.__currentRun]
        pos = [None]*len(d)
        sec = [None]*len(d)
        
        indx = 0
        for x in d:
            pos[indx] = x.pos/10240
            sec[indx] = round(x.sec, 1)
            indx += 1
            
        self.lock.release()
        return [sec, pos]

from dataclasses import dataclass

@dataclass
class posDataEnt:
    pos: int
    sec: int

