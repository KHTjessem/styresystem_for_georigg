import serial
from serial.tools import list_ports as lports
import comStructs
import threading
import atexit

class connection(threading.Thread):
    def __init__(self, comData):
        threading.Thread.__init__(self)
        self.tlock = threading.Lock()

        comport = findComPort()
        self.__serialCon = serial.Serial(comport, timeout=1)
        self.comdata = comData
        self.newComEv = threading.Event()
        self.replyReadyEv = threading.Event()
        atexit.register(self.close)
    
    def write(self, data):
        """Writes the data variable on the serial connection"""
        self.__serialCon.write(data)
        #TODO: set timeout, handle what happens.
        resp = self.__serialCon.read(size=9) #Reply struct is 9 bytes
        if len(resp) < 9:
            return 'Something went wrong'
        return comStructs.reply(resp[0], resp[1], resp[2], resp[3], resp[4:8], resp[8])

    def close(self):
        """Closes the serial connection"""
        self.__serialCon.close()

    def run(self):
        """The main running part of thread."""
        while True:
            self.newComEv.wait()
            r = self.write(self.comdata.getNextCommand())
            self.comdata.newReply(r)
            
            self.newComEv.clear()
            self.replyReadyEv.set()



def findComPort():
    """Returns the comport where the trinamic stepper motor is located"""
    ports = [tuple(port) for port in list(lports.comports())]
    for p in ports:
        if "TMCSTEP" in p[2]: # In our case part of string wil have "TMCSTEP"
            return p[0]