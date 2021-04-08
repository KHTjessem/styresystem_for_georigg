import serial
from serial.tools import list_ports as lports
import comStructs
import threading
import atexit

class connection(threading.Thread):
    def __init__(self, comData):
        threading.Thread.__init__(self)

        comport = findComPort()
        self.__serialCon = serial.Serial(comport, timeout=1)
        self.comdata = comData
        self.newComEv = threading.Event()
        self.replyReadyEv = threading.Event()
        atexit.register(self.close)
    
    def write(self, data):
        self.__serialCon.write(data)
        resp = self.__serialCon.read(size=9) #Reply struct is 9 bytes
        if len(resp) < 9:
            return 'Something went wrong'
        return comStructs.reply(resp[0], resp[1], resp[2], resp[3], resp[4:8], resp[8])

    def close(self):
        self.__serialCon.close()

    def run(self):
        while True:
            self.newComEv.wait()
            r = self.write(self.comdata.getNextCommand())
            self.comdata.newReply(r)
            
            self.newComEv.clear()
            self.replyReadyEv.set()



def findComPort():
    ports = [tuple(port) for port in list(lports.comports())]
    for p in ports:
        if "TMCSTEP" in p[2]: #TODO: add correct name to check for
            return p[0]