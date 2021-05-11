import time
import controll

eng = controll.controll()

done = False
speed = int(input('Give velocity: '))
ant_minut = int(input('Hvor mange minutter kjøretid: '))
minute = 0

while not done:
    print(f'pos nå: {eng.getActualPosition()}')
    eng.rotate_right(speed)
    time.sleep(60)
    eng.stop()
    minute += 1
    pos = eng.getActualPosition()
    print(f'Ved min: {minute} har pos: {pos}')
    input('Press enter for å fortsette videre')
    if minute == ant_minut:
        done = True
eng.stop()
eng.close()