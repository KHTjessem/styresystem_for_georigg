import comSerial
from comStructs import command
import commands as definedCommands
import threading

class controll:
    def __init__(self):
        self.commands = definedCommands.commands()
        self.comdata = comData()
        #self.__connection = comSerial.connection('COM3')
        self.__con = comSerial.connection('COM3', self.comdata)
        self.__con.setDaemon(True)
        self.__con.start()

    # TODO: Might need a lock to make sure only one event at a time
    # Probebly not needed as this will all go in one thread, therefore 
    # it is synced.
    def runCommand(self, command):
        self.comdata.newCommand(command)
        self.__con.newComEv.set()
        self.__con.replyReadyEv.wait() # Can set a timeout. TODO
        self.__con.replyReadyEv.clear()
        #TODO: process the reply and send information to frontend.

    def rotate_right(self, velocity):
        a = self.commands.ROR.newValue(velocity)
        self.runCommand(a)

    def rotate_left(self, velocity):
        a = self.commands.ROL.newValue(velocity)
        self.runCommand(a)
    
    def stop(self):
        self.runCommand(self.commands.MST)
    

    def getActualPosition(self):
        self.runCommand(self.commands.GAP)

    def close(self):
        self.__connection.close()


class comData:
    def __init__(self):
        self.__commands = []
        self.__prioStop = False
        self.lock = threading.Lock()

        self.__reply = None
    
    def newCommand(self, command):
        self.lock.acquire()
        self.__commands.append(command)
        self.lock.release()
    
    def getNextCommand(self):
        self.lock.acquire()
        c = self.__commands.pop()
        self.lock.release()
        return c.getByteArray()
    
    def newReply(self, reply):
        self.lock.acquire()
        self.__reply = reply # maybe turn __reply into a list?
        self.lock.release()
    
    def getReply(self):
        self.lock.acquire()
        r = self.__reply
        self.lock.release()
        return r