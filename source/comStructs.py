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
        #Byte Byte Byte Byte Integer(4 bytes) Byte
        return struct.pack('>BBBBiB',
            self.module_address, self.command_number,
            self.type_number, self.motor_bank, self.value, self.checksum)
    
    def newValue(self, value):
        self.value = value
        self.calckChecksum() #update checksum

def calckChecksum(obj):
    arr = struct.pack('>BBBBi', obj.module_address, obj.command_number, 
                    obj.type_number, obj.motor_bank, obj.value)
    csum = 0
    for b in arr:
        csum += int(b)
    obj.checksum = csum

class reply:
    def __init__(self, reply_address, module_address, status, command_number, value, checksum):
        self.reply_address = reply_address
        self.module_address = module_address
        self.status = status
        self.command_number = command_number
        self.value = value #4 bytes
        self.checksum = checksum
    
    def test(self):
        struct.unpack('>BBBBiB')