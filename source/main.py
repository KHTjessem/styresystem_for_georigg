import eel
import sys
import random
import numpy

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

@eel.expose
def getDataNow():
    return cont.poslog.posData.getAllData()

@eel.expose
def calcVelRPM(rpm):
    vel = round((rpm * 2**3 *200 * 2**8 *2048 * 32)/(16*10**6 * 60))
    rpm = (16*10**6 * vel * 60)/(2**3 * 200* 2**8 *2048 * 32)
    return [vel, rpm]

def close_callback(route, websockets):
    if not websockets:
        cont.stop()
        cont.close()
        exit()

eel.start('index.html')

