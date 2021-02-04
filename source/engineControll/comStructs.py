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
        self.calckChecksum()
    
    def getByteArray(self):
        #Byte Byte Byte Byte Integer(4 bytes) Byte
        return struct.pack('>BBBBiB',
            self.module_address, self.command_number,
            self.type_number, self.motor_bank, self.value, self.checksum)
    
    def calckChecksum(self):
        arr = struct.pack('>BBBBi', self.module_address, self.command_number, 
                        self.type_number, self.motor_bank, self.value)
        csum = 0
        for b in arr:
            csum += int(b)
        self.checksum = csum


class reply:
    def __init__(self, reply_address, module_address, status, value, checksum):
        self.reply_address = reply_address
        self.module_address = module_address
        self.status = status
        self.value = value #4 bytes
        self.checksum = checksum