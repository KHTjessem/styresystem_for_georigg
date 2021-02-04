import serial
import comStructs

# TODO
class connection:
    def __init__(self, comport):
        self.__serialCon = serial.Serial(comport)
    
    def write(self, data):
        self.__serialCon.write(data)
        resp = self.__serialCon.read(size=9) #Reply struct is 9 bytes
        return comStructs.reply(resp[0], resp[1], resp[2], resp[3:7], resp[8])
    
    def close(self):
        self.__serialCon.close()