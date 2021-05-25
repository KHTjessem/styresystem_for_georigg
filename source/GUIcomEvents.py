from events import Events

class eventsList:
    def __init__(self, eel):
        self.eel = eel

        self.evs = Events()
        self.evs.updStatus += self.updStatus
        self.evs.updStatusText += self.updStatusText
        self.evs.updatePosition += self.updPosition
        self.evs.notConneted += self.notConneted
        self.evs.stopEngineEEL += self.stopEngine

    def notConneted(self):
        """Fire when engine is no longer connected"""
        self.eel.notConnected()

    def updStatusText(self, text):
        """Updates status text on GUI"""
        self.eel.updStatusText(text)

    def updStatus(self, status):
        """Updates the status text using 'status' code"""
        self.eel.updStatus(StatusDict[status])

    def updPosition(self, posInmm):
        """Update position on GUI"""
        self.eel.updatePosition(posInmm)
    
    def stopEngine(self):
        """Stops the enigne, does so trough eel
        Usefull to navigate around threads"""
        self.eel.stopEngine()


StatusDict = {
    # self defined
    # THe xx number in the list is self defined.
    # 10: Ready, 20: running, 30: Something went wrong.
    111: [10, 'Connecting to engine'],
    222: [10, 'Connected to engine and ready for use'],
    333: [30, 'Something went wrong'],

    # Based on Command number from TMCL firmware manual 1.42.
    1: [20, 'Extending'],
    2: [20, 'Contracting'],
    3: [10, 'Stopped'],
    4: [20, 'Moving to new position'],
    5: [20, 'Moving to home position']
}