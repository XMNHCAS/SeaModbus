from xmnhModbus.CheckSum import CheckSum
from xmnhModbus.ReadWriteMode import ReadMode
from xmnhModbus.ReadWriteMode import WriteMode


class ReadMessage:

    def GetReadMessage(slaveID: int, readType: ReadMode, startAddr: int,
                       length: int):
        id = int.to_bytes(slaveID, 1, 'big')
        rType = int.to_bytes(readType.value, 1, 'big')
        start = int.to_bytes(startAddr, 2, 'big')
        readLen = int.to_bytes(length, 2, 'big')
        res = [id[0], rType[0], start[0], start[1], readLen[0], readLen[1]]
        checkSum = CheckSum.crc16(res)
        for item in checkSum:
            res.append(item)
        return res


class WriteMessage:

    def WriteSingleColisMessage(slaveID: int, startAddr: int, value: bool):
        id = int.to_bytes(slaveID, 1, 'big')
        wType = int.to_bytes(WriteMode.WriteSingleColis.value, 1, 'big')
        start = int.to_bytes(startAddr, 2, 'big')
        vByte = int.to_bytes(0xff, 2, 'little')
        if (value is not True):
            vByte = int.to_bytes(0x00, 2, 'little')

        res = [id[0], wType[0], start[0], start[1], vByte[0], vByte[1]]
        checkSum = CheckSum.crc16(res)
        for item in checkSum:
            res.append(item)
        return res

    def WriteSingleRegisterMessage():
        print('')

    def WriteMultipleCoilsMessage():
        print('')

    def WriteMultipleRegistersMessage():
        print('')
