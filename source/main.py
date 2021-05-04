import eel
import sys
import random
import platform

from controll import controll
from GUIcomEvents import eventsList

# EEL init
eel.init('web')
events = eventsList(eel)

# Engine init
cont = controll(events)


@eel.expose
def attemptReconnect():
    cont.attemptReconnect()

@eel.expose
def rotate_right(velocity):
    """Makes the engine rotate right vith a speed of velocity (0-2047)"""
    cont.rotate_right(velocity)
@eel.expose
def rotate_left(velocity):
    """Makes the engine rotate left vith a speed of velocity (0-2047)"""
    cont.rotate_left(velocity)
@eel.expose
def moveto_rel(dist):
    """Move engine with relative distance. provide dist in mm"""
    dist = round(dist*10240) # convert to microsteps
    print(f'rel move: {dist}')
    cont.moveto_rel(dist)
@eel.expose
def moveto_abs(pos):
    """Moves the engine to absolute position. pos is in mm"""
    pos = round(pos*10240) # convert to microsteps
    print(f'moving to {pos}')
    cont.moveto_abs(pos)


@eel.expose
def setHome():
    """Set current engine position as home"""
    cont.setHome()

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



eel_kwargs = dict(
    host='localhost',
    port=8080,
    size=(1280, 800),
)

# Browser fallback for windows.
# All windows machine should come with edge
try:
    eel.start('index.html', **eel_kwargs)
except EnvironmentError:
    # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
    if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
        eel.start('index.html', mode='edge', **eel_kwargs)
    else:
        raise

