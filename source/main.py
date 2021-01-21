import eel
import sys

import random

eel.init('web')


@eel.expose
def rand_numb():
    return random.randint(0, 100)


eel.start('index.html')