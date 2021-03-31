import serial
import comStructs
import threading
import atexit

class connection(threading.Thread):
    def __init__(self, comport, comData):
        self.__serialCon = serial.Serial(comport)
        self.comdata = comData
        self.newComEv = threading.Event()
        self.replyReadyEv = threading.Event()
    
    def write(self, data):
        self.__serialCon.write(data)
        resp = self.__serialCon.read(size=9) #Reply struct is 9 bytes
        return comStructs.reply(resp[0], resp[1], resp[2], resp[3], resp[4:8], resp[8])

    @atexit.register #TODO: check if this works.
    def close(self):
        self.__serialCon.close()

    def run(self):
        while True:
            self.newComEv.wait()
            r = self.write(self.comdata.getNextCommand())
            self.comdata.newReply(r)
            
            self.newComEv.clear()
            self.replyReadyEv.set()

