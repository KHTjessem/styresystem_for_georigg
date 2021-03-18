import eel

eel.init('web')

@eel.expose
def dummy():
    1 + 1

eel.start('index.html')