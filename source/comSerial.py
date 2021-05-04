import serial
from serial.tools import list_ports as lports
import comStructs
import threading
import atexit

class connection(threading.Thread):
    def __init__(self, comData, statusCommand):
        threading.Thread.__init__(self)
        self.tlock = threading.Lock()
        self.statCommand = statusCommand

        self.comport = findComPort()
        self.connected = False
        self.__serialCon = None
        if self.comport is not None:
            self.connect()


        self.comdata = comData
        self.newComEv = threading.Event()
        self.replyReadyEv = threading.Event()
        atexit.register(self.close)

    def run(self):
        """The main running part of thread."""
        while True:
            self.newComEv.wait()
            r = self.write(self.comdata.getNextCommand())
            self.comdata.newReply(r)
            self.newComEv.clear()
            self.replyReadyEv.set()
    
    def write(self, data):
        """Writes the data variable on the serial connection"""
        if not self.connected:
            return "Not connected to engine"
        print(f'Writing command: {data}')
        self.__serialCon.write(data)
        resp = self.__serialCon.read(size=9) #Reply struct is 9 bytes
        print(f'Response: {resp}')
        if len(resp) < 9:
            return self.checkConnection(data)
        return comStructs.reply(resp[0], resp[1], resp[2], resp[3], resp[4:8], resp[8])

    def checkConnection(self, data):
        """Checks if engine has some error or lost connection"""
        cport = findComPort()
        if cport is None:
            return "Cant find engine, is it connected?"
        self.comport = cport
        try:
            # Attempt reconnect
            self.close()
            self.connect()

            self.__serialCon.write(data)
            resp = self.__serialCon.read(size=9)
            if len(resp) == 9:
                return resp
        except:
            pass

        self.__serialCon.write(self.statCommand.getByteArray())
        resp = self.__serialCon.read(size=9)
        if len(resp) == 9:
            return "Unable to connect" # Last ditch effort is to restart thread.



    def connect(self):
        try:
            self.__serialCon = serial.Serial(self.comport, timeout=0.5)
            self.connected = True
        except:
            pass
        finally:
            pass
    
    def close(self):
        """Closes the serial connection"""
        try:
            self.__serialCon.close()
        except:
            pass



def findComPort():
    """Returns the comport where the trinamic stepper motor is located"""
    ports = [tuple(port) for port in list(lports.comports())]
    for p in ports:
        if "TMCSTEP" in p[2]: # In our case part of string wil have "TMCSTEP"
            return p[0]
    return None