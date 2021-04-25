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
    """Makes the engine rotate right vith a speed of velocity (0-2047)"""
    cont.rotate_right(velocity)
@eel.expose
def rotate_left(velocity):
    """Makes the engine rotate left vith a speed of velocity (0-2047)"""
    cont.rotate_left(velocity)
@eel.expose
def stop():
    """Stops the enigne"""
    cont.stop()

@eel.expose
def getDataNow(): #TODO: fix it
    return cont.poslog.posData.getLatestData()

@eel.expose
def calcVelRPM(rpm):
    """
    Calculates the rpm that fits, an translates it to engine values.
    Returns [velocity value, rpm value].
    """
    vel = round((rpm * 2**3 *200 * 2**8 *2048 * 32)/(16*10**6 * 60))
    rpm = (16*10**6 * vel * 60)/(2**3 * 200* 2**8 *2048 * 32)
    return [vel, round(rpm, 2)]

# def close_callback(route, websockets):# TODO: probebly not needed. not currently in use
#     if not websockets:
#         cont.stop()
#         cont.close()
#         exit()

eel.start('index.html')

