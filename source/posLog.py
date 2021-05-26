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
        self.prevposCount = 0
        self.totLength = 0
        self.maxleft = -614400
        self.maxright = 614400
    

    def run(self):
        """Main running loop of thread"""
        while True:
            self.newRunEV.wait()
            # Wait() is wrongly triggered when running clear(),
            # this fixes the issue, not to happy about it.
            time.sleep(0.1)
            if not self.newRunEV.is_set():
                continue
            print('New run')
            self.newRun()
            self.work()
            self.newRunEV.clear()

    def work(self):
        """Threads main workload"""
        while self.newRunEV.is_set():
            t = self.timeKeep()
            p = self.posKeep()
            if not t or not p:
                break      
            time.sleep(self.waitTime)
        

    def posKeep(self):
        pos = self.getPos()
        if pos is not None:
            self.evs.evs.updatePosition(pos/10240) # 10240 microsteps = 1 mm displacement
        elif pos is None:
            # Possably lost connection
            self.newRunEV.clear()
            return False
        if pos == self.prevPos:
            self.prevposCount += 1
            if self.prevposCount >= 4:
                self.prevposCount = 0
                self.newRunEV.clear()
                self.evs.evs.updStatus(3)
        else:
            if self.prevPos is not None:
                self.totLength += abs(self.prevPos - pos)
            self.prevPos = pos
            self.prevposCount = 0
            
        if self.maxleft != 0 and pos <= self.maxleft:
            print(f'Reached Max left: {self.maxleft}, pos: {pos}')
            self.stopEng('Reached max extension')
            return False
        elif self.maxright != 0 and pos >= self.maxright:
            print(f'Reached Max right: {self.maxright}, pos: {pos}')
            self.stopEng('Reached max contraction')
            return False
        return True

    def timeKeep(self):
        t = time.time() - self.__startTime
        self.totTime = int(t) #Rounds it down
        self.evs.timePassed(self.totTime)
        # print(f'Total time: {self.totTime}, t: {t}, maxT: {self.maxTime}')
        if  self.maxTime != 0 and self.totTime >= self.maxTime: #No more time left.
            self.newRunEV.clear()
            self.stopEng('Max runtime reached')
            return False
        return True
    

    def stopEng(self, msg):
        self.newRunEV.clear()
        self.evs.stopEngine()
        time.sleep(0.5)
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
            self.evs.notConneted()
            return None
        return pos.value

    
    def newRun(self):
        """Start from 0 again"""
        self.__startTime = time.time()
        self.totTime = 0


    def stop(self):
        """Stops the main loop"""
        self.newRunEV.clear()


