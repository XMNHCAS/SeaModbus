from CheckSum import CheckSum
from ReadWriteMode import ReadWriteMode


class ReadMessageFunction:

    def GetReadMessage(slaveID: int, readType: ReadWriteMode, startAddr: int,
                       length: int):
        id = int.to_bytes(slaveID, 1, 'big')
        readType = int.to_bytes(readType.value, 1, 'big')
        start = int.to_bytes(startAddr, 2, 'big')
        readLen = int.to_bytes(length, 2, 'big')
        res = [id[0], readType[0], start[0], start[1], readLen[0], readLen[1]]
        checkSum = CheckSum.crc16(res)
        for item in checkSum:
            res.append(item)
        return res
