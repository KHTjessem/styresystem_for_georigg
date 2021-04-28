from events import Events

class eventsList:
    def __init__(self, eel):
        self.eel = eel

        evs = Events()
        evs.updStatus += self.updStatus
        evs.updStatusText += self.updStatusText
        evs.updatePosition += self.updPosition


    def updStatusText(self, text):
        """Updates status text on GUI"""
        self.eel.updStatusText(text)

    def updStatus(self, status):
        """Updates the status text using 'status' code"""
        self.eel.updStatus(StatusDict[status])

    def updPosition(self, posInmm):
        """Update position on GUI"""
        self.eel.updatePosition(posInmm)

StatusDict = {
    # self defined
    # THe xx number in the list is self defined.
    # 10: Ready, 20: running, 30: Something went wrong.
    111: [10, 'Connecting to engine'],
    222: [10, 'Connected to engine and ready for use'],
    333: [30, 'Something went wrong'],

    # Based on Command number from TMCL firmware manual 1.42.
    1: [20, 'Rotating right'],
    2: [20, 'Rotating left'],
    3: [10, 'Stoped']
}