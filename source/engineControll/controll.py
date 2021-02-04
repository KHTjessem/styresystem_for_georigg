import comSerial
from comStructs import command

# TODO: implement all controll commands.
class controll:
    def __init__(self):
        self.__connection = comSerial.connection('COM3')

    
    # For now harcoded numbers, needs to be changed.
    # Supposed to be the command:
    #   Rotate left motor 0, velocity 10.
    #   Mnemonic: ROL 0, 10.
    def rotate_left(self):
        ROL = command(1, 2, 0, 0, -100)
        self.__connection.write(ROL.getByteArray())
    
    def stop(self):
        MST = command(1, 3, 0, 0, 0)
        self.__connection.write(MST.getByteArray())
    
    def close(self):
        self.__connection.close()


if __name__ == "__main__":
    c = controll()
    c.rotate_left()
    c.stop()
    c.close()