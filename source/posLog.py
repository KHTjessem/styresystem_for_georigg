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

        self.__startTime = None
        self.totTime = 0
        self.maxTime = maxtime
        self.waitTime = waitTime

        self.prevPos = None
        self.totLength = 0
        self.maxleft = -614400
        self.maxright = 614400
    

    def run(self):
        """Main running loop of thread"""
        while True:
            self.newRunEV.wait()
            self.newRun()
            self.work()
            self.newRunEV.clear()
    
    def work(self):
        """Threads main workload"""
        while self.newRunEV.is_set():
            t = time.time() - self.__startTime
            self.totTime += t
            pos = self.getPos()
            if pos is not None:
                self.evs.evs.updatePosition(pos/10240) # 10240 microsteps = 1 mm displacement
            if pos == self.prevPos:
                self.newRunEV.clear()
                self.evs.evs.updStatus(3)
            else:
                if self.prevPos is not None:
                    self.totLength += abs(self.prevPos - pos)
                self.prevPos = pos
            if self.totTime >= self.maxTime and self.maxTime > 0: #No more time left.
                self.stopEng('Max runtime reached')
            elif self.maxleft < 0 and pos <= self.maxleft:
                self.stopEng('Reached max extension')
            elif self.maxright > 0 and pos <= self.maxright:
                self.stopEng('Reached max contraction')
            else:
                time.sleep(self.waitTime)

    def stopEng(self, msg):
        self.newRunEV.clear()
        self.evs.stopEngineEEL()
        self.evs.updStatusText(msg)

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
        self.__startTime = time.time()


    def stop(self):
        """Stops the main loop"""
        self.newRunEV.clear()


