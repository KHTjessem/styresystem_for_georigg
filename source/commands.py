from comStructs import command

# TODO: implement all controll commands.

# adress and choice of motor/axis is hardcoded.
# TODO: get module adress, engine/axis etc from "dynamic" source
class commands:
    def __init__(self):
        # module_address, command_number, type_number, motor_bank, value
        #           command(1,1, 0, 0, 0)

        # Movement
        self.ROR = command(1,1, 0, 0, 0)
        self.ROL = command(1, 2, 0, 0, 0)
        self.MST = command(1, 3, 0, 0, 0)
        self.MVP = command (1, 4, 0, 0, 0) # Type, 0: absolute, 1: relative, 2: coordinate.

        # Get and set information
        self.SAP = command(1, 5, 1, 0, 0) # Set axis parameter
        self.GAP = command(1, 6, 1, 0, 0) # Get axis parameter
        