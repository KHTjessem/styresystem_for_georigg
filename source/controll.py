import comSerial
from comStructs import command
from posLog import posLogger
import commands as definedCommands
import threading, time

class controll:
    def __init__(self, events):
        self.commands = definedCommands.commands()
        self.comdata = comData()
        self.events = events
        self.events.evs.updStatus(111)

        self.lastCommand = None

        # Connection on its own thread
        self.__con = None
        self.setUpConnection()
        
        # Position trakcer & time keeper on its own thread.
        self.poslog = posLogger(self.__con, self.comdata, 0.2, self.commands.GAP, self.events)
        self.poslog.setDaemon(True)
        self.poslog.start()
        self.logpos = False
    
    def setUpConnection(self):
        self.__con = comSerial.connection(self.comdata)
        self.__con.setDaemon(True)
        self.__con.start()
        if not self.__con.connected:
            self.events.evs.notConneted()
            time.sleep(0.2)
            e = self.comdata.geterrorMsg()
            if e is not None:
                self.events.updStatusText(e)
                self.comdata.newError(None)
        else:
            self.events.evs.updStatus(222)
    
    def attemptReconnect(self):
        print("attempting to reconnect")
        port = comSerial.findComPort()
        if port is None:
            print("Comport not found")
            self.events.evs.updStatus(333)
            self.events.evs.updStatusText("Unable to find engine, is it connected?")
            self.events.evs.notConnected()
            return False
        e = self.comdata.geterrorMsg()
        if e is not None:
            self.events.updStatusText(e)
            self.comdata.newError(None)
            return False
        self.__con.connect()
        # If engine is running wil stop if above max limit after reconnect
        self.poslog.newRunEV.set()
        self.events.evs.updStatus(222)
        return True
        

    def runCommand(self, command):
        """Runs the command, response is in self.comdata"""
        self.__con.tlock.acquire()
        if self.__con.connected:
            self.checkLogging()
            self.lastCommand = command
            self.comdata.newCommand(command)
            self.__con.newComEv.set()
            self.__con.replyReadyEv.wait()
            self.handleReply()
            self.__con.replyReadyEv.clear()
        else:
            self.events.evs.notConneted()
            self.logpos = False
            self.poslog.newRunEV.clear()
        self.__con.tlock.release()
    
    def checkLogging(self):
        """Checks if logger should be on or off and sets it accordingly."""
        if self.logpos and self.poslog.newRunEV.is_set():
            print('wrong')
            return
        self.poslog.newRunEV.set()
    
    def handleReply(self):
        """Handles the reply from engines module"""
        rep = self.comdata.getReply()
        if rep == "Not connected to engine":
            self.events.evs.notConneted()
            return
        if isinstance(rep, str):
            return self.events.updStatusText(rep)
        if rep.status == 100:
            if self.lastCommand.type_number == 154 or self.lastCommand.type_number == 4:
                return
            self.events.evs.updStatus(rep.command_number)
        if rep.command_number == 6:
            self.events.evs.updPosition(rep.value/10240)
        
    


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
        #self.poslog.newRunEV.clear()
    
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
        """Collects the enignes position in microsteps."""
        self.runCommand(self.commands.GAP)

    # Test if this works. Race condition should not matter because
    # The value only gets set from here, on its class its only read. 
    # The reading happens evry x amount of time, therefore if it changes in a race condition,
    # The new value will get read at next run through.

    def newMaxValues(self, left, right):
        """Set max left and right extension"""
        self.poslog.maxleft = left * 10240
        self.poslog.maxright = right * 10240

    def newMaxTime(self, time):
        """Sets max runtime, 'time' needs to be in seconds"""
        self.poslog.maxTime = time


class comData:
    def __init__(self):
        self.__command = None
        self.lock = threading.Lock()
        self.errorMsg = None

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
    
    def newError(self, msg):
        """Set new error message"""
        self.lock.acquire()
        self.errorMsg = msg
        self.lock.release()
    
    def geterrorMsg(self):
        """Get the latest error message"""
        self.lock.acquire()
        e = self.errorMsg
        self.lock.release()
        return e