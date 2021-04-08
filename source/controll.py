import comSerial
from comStructs import command
import commands as definedCommands
import threading

class controll:
    def __init__(self, events):
        self.commands = definedCommands.commands()
        self.comdata = comData()
        self.events = events
        self.events['updStatus'].trigger(111)
        self.__con = comSerial.connection(self.comdata)
        self.__con.setDaemon(True)
        self.__con.start()
        self.events['updStatus'].trigger(222)

    # TODO: Might need a lock to make sure only one event at a time
    # Probably not needed as this will all go in one thread, therefore 
    # it is synced.
    def runCommand(self, command):
        self.comdata.newCommand(command)
        self.__con.newComEv.set()
        self.__con.replyReadyEv.wait() # Can set a timeout. TODO
        self.events['updStatus'].trigger(command.command_number)
        #TODO: process the reply and send information to frontend.
        self.handleReply()
        self.__con.replyReadyEv.clear()
    
    def handleReply(self):
        pass #TODO
        #self.events['updStatusText'].trigger('Success')


    def rotate_right(self, velocity):
        self.commands.ROR.newValue(velocity)
        self.runCommand(self.commands.ROR)

    def rotate_left(self, velocity):
        self.commands.ROL.newValue(velocity)
        self.runCommand(self.commands.ROL)
    
    def stop(self):
        self.runCommand(self.commands.MST)
    

    def getActualPosition(self):
        self.runCommand(self.commands.GAP)


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
        if self.__prioStop:
            raise NotImplementedError # TODO: implement
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