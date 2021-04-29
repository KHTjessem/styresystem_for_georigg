import struct
# Information from TMCM-1611 datasheet
# https://www.trinamic.com/products/modules/details/tmcm-1161/

class command:
    def __init__(self, module_address, command_number, type_number, motor_bank, value):
        self.module_address = module_address
        self.command_number = command_number
        self.type_number = type_number
        self.motor_bank = motor_bank
        self.value = value # 4Bytes
        self.checksum = None
        calckChecksum(self)
    
    def getByteArray(self):
        """Returns its own values in a bytearray as specified in TMCM-1611 datasheet"""
        return gba(self)
    
    def newValue(self, value):
        """Set a new value for command"""
        self.value = value
        calckChecksum(self) #update checksum

def gba(obj):
    #Byte Byte Byte Byte Integer(4 bytes) Byte
    return struct.pack('>BBBBiB',
        obj.module_address, obj.command_number,
        obj.type_number, obj.motor_bank, obj.value, obj.checksum)

def calckChecksum(obj): #TODO: check if works
    """Calculates a objects checksum and sets it"""
    arr = struct.pack('>BBBBi', obj.module_address, obj.command_number, 
                    obj.type_number, obj.motor_bank, obj.value)
    csum = arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7]
    obj.checksum = csum

class reply:
    def __init__(self, reply_address, module_address, status, command_number, value, checksum):
        self.reply_address = reply_address
        self.module_address = module_address
        self.status = status
        self.command_number = command_number
        self.value = int.from_bytes(value, byteorder="big") #4 bytes
        self.checksum = checksum
    
    def test(self):
        struct.unpack('>BBBBiB')