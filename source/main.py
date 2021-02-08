import eel
import sys

import random

from engineControll.controll import controll

# Engine init
cont = controll()

# EEL init
eel.init('web')

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
def rand_numb():
    return random.randint(0, 100)


def close_callback(route, websockets):
    if not websockets:
        cont.stop()
        cont.close()
        exit()

eel.start('index.html', close_callback=close_callback)

