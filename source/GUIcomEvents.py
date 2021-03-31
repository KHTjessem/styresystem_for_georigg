from events import Events

class eventsList:
    def __init__(self, eel):
        self.eel = eel
        a = Events()
        a.trigger += self.updStatusText
        self.evDict = {
            'updStatusText': a
        }


    def updStatusText(self, text):
        self.eel.updStatusText(text)