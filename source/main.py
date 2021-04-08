import eel
import sys
import random

from controll import controll
from GUIcomEvents import eventsList

# EEL init
eel.init('web')
events = eventsList(eel)

# Engine init
cont = controll(events.evDict)

@eel.expose
def rotate_right(velocity):
    cont.rotate_right(velocity)
@eel.expose
def rotate_left(velocity):
    cont.rotate_left(velocity)
@eel.expose
def stop():
    cont.stop()




def close_callback(route, websockets):
    if not websockets:
        cont.stop()
        cont.close()
        exit()

eel.start('index.html')

