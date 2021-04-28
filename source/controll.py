import comSerial
from comStructs import command
from posLog import posLogger
import commands as definedCommands
import threading

class controll:
    def __init__(self, events):
        self.commands = definedCommands.commands()
        self.comdata = comData()
        self.lock = threading.Lock() # Needed so only one commands runs at a time
        self.events = events
        self.events.evs.updStatus(111)

        # Connection on its own thread
        self.__con = comSerial.connection(self.comdata)
        self.__con.setDaemon(True)
        self.__con.start()
        
        # Position trakcer & time keeper on its own thread.
        self.poslog = posLogger(self.__con, self.comdata, 1, self.commands.GAP, self.events)
        self.poslog.setDaemon(True)
        self.poslog.start()
        self.logpos = False

        self.events.evs.updStatus(222)

    # TODO: Might need a lock to make sure only one event at a time
    # Probably not needed as this will all go in one thread, therefore 
    # it is synced.
    def runCommand(self, command):
        """Runs the command, response is in self.comdata"""
        self.checkLogging()
        self.__con.tlock.acquire()
        self.comdata.newCommand(command)
        self.__con.newComEv.set()
        self.__con.replyReadyEv.wait() # Can set a timeout. TODO
        self.events.evs.updStatus(command.command_number)
        #TODO: process the reply and send information to frontend.
        self.handleReply()
        self.__con.replyReadyEv.clear()
        self.__con.tlock.release()
    
    def checkLogging(self):
        """Checks if logger should be on or off and sets it accordingly."""
        if self.logpos and self.poslog.newRunEV.is_set():
            return
        self.poslog.newRunEV.set()
    
    def handleReply(self):
        """Not implemented"""
        pass #TODO
        #self.events['updStatusText'].trigger('Success')


    def rotate_right(self, velocity):
        """Prepeares and then runs the rotate right command"""
        self.logpos = True
        self.commands.ROR.newValue(velocity)
        self.runCommand(self.commands.ROR)

    def rotate_left(self, velocity):
        """Prepeares and then runs the rotate left command"""
        self.logpos = True
        self.commands.ROL.newValue(velocity)
        self.runCommand(self.commands.ROL)
    
    def stop(self):
        """Stops the engine, stops logpos"""
        self.logpos = False
        self.runCommand(self.commands.MST)
        self.poslog.newRunEV.clear()
    

    def getActualPosition(self):
        """Collects the enignes position in microsteps. TODO: handle reply"""
        self.runCommand(self.commands.GAP)
        return self.comdata.getReply() #TODO: Make sure it will always get right reply.


class comData:
    def __init__(self):
        self.__commands = []
        self.__prioStop = False
        self.lock = threading.Lock()

        self.__reply = None
    
    def newCommand(self, command): # Potential TODO: command does not need to be a list.
        """Add command to list."""
        self.lock.acquire()
        self.__commands.append(command)
        self.lock.release()
    
    def getNextCommand(self):
        """Get the next command to run"""
        self.lock.acquire()
        if self.__prioStop:
            raise NotImplementedError # TODO: implement
        c = self.__commands.pop()
        self.lock.release()
        return c.getByteArray()
    
    def newReply(self, reply):
        """Set the reply"""
        self.lock.acquire()
        self.__reply = reply # maybe turn __reply into a list?
        self.lock.release()
    
    def getReply(self):
        """Get latest reply"""
        self.lock.acquire()
        r = self.__reply
        self.lock.release()
        return r