from theThreaded import counter as c
import threading


class tester:
    def __init__(self, events):
        self.evList = events
        self.newNumEv = threading.Event()
        self.comdata = comdata()
        self.__c = c(self.newNumEv, self.comdata, events)
        self.__c.setDaemon(True)
        self.__c.start()

        self.lock = threading.Lock()


    def getNewNum(self):
        print('stress test')
        for i in range(99):
            print(f'Triggering run command event, My thread: {threading.get_ident()}')
            self.__c.newNumEvent.set()
            self.__c.comEvent.wait()
            self.__c.comEvent.clear()
            n = self.comdata.getNum()
            print(f'Sending n:{n}')
            self.evList['jsmsg'].trigger(n)



class comdata:
    def __init__(self):
        self.__num = 0
        self.lock = threading.Lock()
    
    def getNum(self):
        self.lock.acquire()
        n = self.__num
        self.lock.release()
        return n
    
    def incNum(self):
        self.lock.acquire()
        self.__num += 1
        self.lock.release()

    def setNum(self, num):
        self.lock.acquire()
        self.__num = num
        self.lock.release()
