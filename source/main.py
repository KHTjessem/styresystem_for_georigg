import eel

import controller as cont
import myEvents

eel.init('web')

#Events
evs = myEvents.mightWork(eel)


plz = cont.tester(evs.evnetHandlers)

@eel.expose
def dummy():
    pass


@eel.expose
def getNum():
    return plz.getNewNum()

eel.start('index.html')