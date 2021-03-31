import time
import random
import threading
from events import Events


class counter(threading.Thread):
    """
    This class will 'simulate' communication over serial connection,
    for now does this with just increasing a number.
    """
    def __init__(self, newNumEvent, comdata, crosstest):
        threading.Thread.__init__(self)
        self.newNumEvent = newNumEvent
        self.comEvent = threading.Event()

        self.comdata = comdata
        self.crosstest = crosstest

    def run(self):
        # event with no timeout should be locked.
        while True:
            self.newNumEvent.wait()
            print(f'generating new num, My thread: {threading.get_ident()}')
            self.work()
            time.sleep(0.2)
            self.newNumEvent.clear()
            self.comEvent.set()

    def work(self):
        svar = self.new_num()
        self.comdata.setNum(svar)

    def new_num(self):
        return random.randint(0,5)

