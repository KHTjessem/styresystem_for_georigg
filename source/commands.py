from comStructs import command

class commands:
    def __init__(self):
        self.madd = 1
        self.mbank = 0
        # module_address, command_number, type_number, motor_bank, value
        #           command(1,1, 0, 0, 0)

        # Movement
        self.ROR = command(self.madd, 1, 0, self.mbank, 0)
        self.ROL = command(self.madd, 2, 0, self.mbank, 0)
        self.MST = command(self.madd, 3, 0, self.mbank, 0)
        self.MVP = command(self.madd, 4, 0, self.mbank, 0) # Type, 0: absolute, 1: relative, 2: coordinate.

        # Get and set information
        self.SAP = command(self.madd, 5, 1, self.mbank, 0) # Set axis parameter
        self.ChangePdiv = command(self.madd, 5, 154, self.mbank, 0)



        self.GAP = command(self.madd, 6, 1, self.mbank, 0) # Get axis parameter
            # TMCL_firmware_manual page 32 for full type info
            # https://www.trinamic.com/products/modules/details/tmcm-1161/
            ## type: 4: max speed, 5: max accel, 154: pulse divisor
        self.STAP = command(self.madd, 7, 1, self.mbank, 0)

        # Used to get engines status.
        self.DriveStatusFlags = command(self.madd, 6, 208, self.mbank, 0)