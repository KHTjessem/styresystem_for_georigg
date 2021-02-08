import comSerial
from comStructs import command

# TODO: implement all controll commands.
class controll:
    def __init__(self):
        self.__connection = comSerial.connection('COM3')

    
    # adress and choice of motor/axis is hardcoded.
    # TODO: get module adress, engine/axis etc from "dynamic" source
    def rotate_right(self, velocity):
        ROR = command(1,1, 0, 0, velocity)
        return self.__connection.write(ROR.getByteArray())

    def rotate_left(self, velocity):
        ROL = command(1, 2, 0, 0, velocity)
        s = self.__connection.write(ROL.getByteArray())
        print(s)
    
    def stop(self):
        MST = command(1, 3, 0, 0, 0)
        s = self.__connection.write(MST.getByteArray())
        print(s)
    

    def getActualPosition(self):
        GAP = command(1, 6, 1, 0, 0)
        s = self.__connection.write(GAP.getByteArray())
        print("Position: " + str(int.from_bytes(s.value, 'big', signed=True)))
        print(str(s.value))

    def close(self):
        self.__connection.close()
