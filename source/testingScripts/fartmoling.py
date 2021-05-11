import time
import controll

eng = controll.controll()

done = False
speed = int(input('Give velocity: '))
ant_sek = int(input('Hvor mange sekunder kjøretid: '))
sek = 0

data = []

pos = eng.getActualPosition()
data.append(pos)
print(f'pos ved 0: {pos}')

eng.rotate_right(speed)
while not done:
    time.sleep(1)
    pos = eng.getActualPosition()
    data.append(pos)
    print(f'pos nå: {pos}')
    sek += 1
    if sek == ant_sek:
        done = True
eng.stop()
eng.close()

print('=====DATA=====')
print(data)
print('==============')