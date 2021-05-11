import serial, time
from comStructs import command, reply

serialCon = serial.Serial('COM3', timeout=0.5)

ror = command(1, 1, 0, 0, 89)
stop = command(1, 3, 0, 0, 0)
data = ror.getByteArray()

print(f'Writing command: {data}')
serialCon.write(data)
resp = serialCon.read(size=9) #Reply struct is 9 bytes
r = reply(resp[0], resp[1], resp[2], resp[3], resp[4:8], resp[8])
print(f'Response: {resp}, replyStatus {r.status}')

time.sleep(5) # sleep 5 seconds

stopBArray = stop.getByteArray()
print(f'Writing command: {stopBArray}')
serialCon.write(stopBArray)
resp = serialCon.read(size=9) #Reply struct is 9 bytes
r = reply(resp[0], resp[1], resp[2], resp[3], resp[4:8], resp[8])
print(f'Response: {resp}, replyStatus {r.status}')




