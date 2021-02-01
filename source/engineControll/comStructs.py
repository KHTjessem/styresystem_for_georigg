# Information from TMCM-1611 datasheet
# https://www.trinamic.com/products/modules/details/tmcm-1161/

class command:
    def __init__(self, module_address, command_number, type_number, value, checksum):
        self.module_address = module_address
        self.command_number = command_number
        self.type_number = type_number
        self.value = value # 4Bytes
        self.checksum = checksum

class reply:
    def __init__(self, reply_address, module_address, status, value, checksum):
        self.reply_address = reply_address
        self.module_address = module_address
        self.status = status
        self.value = value #4 bytes
        self.checksum = checksum