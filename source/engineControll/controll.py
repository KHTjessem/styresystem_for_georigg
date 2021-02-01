import comSerial
from comStructs import command

# TODO: implement all controll commands.
class controll:
    def __init__(self):
        self.__connection = comSerial.connection('COM3')

    
    # For now harcoded numbers, needs to be changed.
    # Supposed to be the command:
    #   Rotate left motor 0, velocity 1000.
    #   Mnemonic: ROL 0, 1000.
    def rotate_left(self):
        ROL = command(1, 2, 0, 1000, 238)
        self.__connection.write(ROL)