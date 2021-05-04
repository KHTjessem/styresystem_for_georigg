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
        self.__con = None
        self.setUpConnection()
        
        # Position trakcer & time keeper on its own thread.
        self.poslog = posLogger(self.__con, self.comdata, 0.2, self.commands.GAP, self.events)
        self.poslog.setDaemon(True)
        self.poslog.start()
        self.logpos = False
    
    def setUpConnection(self):
        self.__con = comSerial.connection(self.comdata, self.commands.DriveStatusFlags)
        self.__con.setDaemon(True)
        self.__con.start()
        if not self.__con.connected:
            self.events.evs.notConneted()
        else:
            self.events.evs.updStatus(222)
    
    def attemptReconnect(self):
        port = comSerial.findComPort()
        if port is None:
            self.events.evs.updStatus(333)
            self.events.evs.updStatusText("Unable to find engine, is it connected?")
            self.events.evs.notConnected()
            return False
        

    def runCommand(self, command):
        """Runs the command, response is in self.comdata"""
        self.__con.tlock.acquire()
        if self.__con.connected:
            self.checkLogging()
            self.comdata.newCommand(command)
            self.__con.newComEv.set()
            self.__con.replyReadyEv.wait()
            self.events.evs.updStatus(command.command_number)
            self.handleReply()
            self.__con.replyReadyEv.clear()
        else:
            self.events.evs.notConneted()
        self.__con.tlock.release()
    
    def checkLogging(self):
        """Checks if logger should be on or off and sets it accordingly."""
        if self.logpos and self.poslog.newRunEV.is_set():
            return
        self.poslog.newRunEV.set()
    
    def handleReply(self):
        """Not implemented"""
        rep = self.comdata.getReply()
        if rep == "Not connected to engine":
            return self.events.evs.notConneted()
    


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
    
    def moveto_abs(self, pos):
        """Move to absolute position. pos is in microsteps"""
        self.commands.MVP.newTypeAndValue(0, pos)
        self.runCommand(self.commands.MVP)
    
    def moveto_rel(self, amount):
        """Moves the engine relative"""
        self.commands.MVP.newTypeAndValue(1, amount)
        self.runCommand(self.commands.MVP)
    
    def stop(self):
        """Stops the engine, stops logpos"""
        self.logpos = False
        self.runCommand(self.commands.MST)
        self.poslog.newRunEV.clear()
    
    def setPdiv(self, pdiv):
        """Change the modules Pulse divisor"""
        self.commands.ChangePdiv.newValue(pdiv)
        self.runCommand(self.commands.ChangePdiv)

    def setHome(self):
        """Sets current position as new home position"""
        self.commands.SAP.newTypeAndValue(1, 0)
        self.runCommand(self.commands.SAP)
    
    def setMaxSpeedPmode(self, maxVel):
        """Set the maximum speed in positioning mode"""
        self.commands.SAP.newTypeAndValue(4, maxVel)
        self.runCommand(self.commands.SAP)

    def getActualPosition(self):
        """Collects the enignes position in microsteps. TODO: handle reply"""
        self.runCommand(self.commands.GAP)


class comData:
    def __init__(self):
        self.__command = None
        self.lock = threading.Lock()

        self.__reply = None
    
    def newCommand(self, command):
        """Add command to list."""
        self.lock.acquire()
        self.__command = command
        self.lock.release()
    
    def getNextCommand(self):
        """Get the next command to run"""
        self.lock.acquire()
        c = self.__command
        self.lock.release()
        return c.getByteArray()
    
    def newReply(self, reply):
        """Set the reply"""
        self.lock.acquire()
        self.__reply = reply
        self.lock.release()
    
    def getReply(self):
        """Get latest reply"""
        self.lock.acquire()
        r = self.__reply
        self.lock.release()
        return r