from events import Events
import threading

class mightWork:
    def __init__(self, eel):
        self.eel = eel
        a = Events()
        a.trigger += self.JSMessage
        self.evnetHandlers = {
            'jsmsg': a
        }
    

    def JSMessage(self, mssg):
        print(f'sending jsmsg, My thread: {threading.get_ident()}')
        print(f'msg: {mssg}')
        self.eel.jsmsg(mssg)


        