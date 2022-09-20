import sys


class CheckSum:

    def crc16(data: list):
        try:
            crc = 0xffff
            for item in data:
                crc = crc ^ item
                for i in range(8):
                    if (crc & 1) == 1:
                        crc = (crc >> 1) ^ 0xa001
                    else:
                        crc = crc >> 1
            highBit = (crc & 0xff00) >> 8
            lowBit = crc & 0x00ff
            if sys.byteorder.capitalize() == 'Little':
                return [lowBit, highBit]
            else:
                return [highBit, lowBit]
        except Exception as err:
            print(err)
            return [0x00, 0x00]
