import serial, time
from comStructs import command

serialCon = serial.Serial('COM3', timeout=0.5)

ror = command(1, 1, 0, 0, 89)
stop = command(1, 3, 0, 0, 0)
data = ror.getByteArray()

print(f'Writing command: {data}')
serialCon.write(data)
resp = serialCon.read(size=9) #Reply struct is 9 bytes
print(f'Response: {resp}')

time.sleep(20) # sleep 20 seconds

stopBArray = stop.getByteArray()
print(f'Writing command: {stopBArray}')
serialCon.write(stopBArray)
resp = serialCon.read(size=9) #Reply struct is 9 bytes
print(f'Response: {resp}')




