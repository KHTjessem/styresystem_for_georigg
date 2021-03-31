import serial
import comStructs
import threading
import atexit

class connection(threading.Thread):
    def __init__(self, comport, comData):
        threading.Thread.__init__(self)
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

