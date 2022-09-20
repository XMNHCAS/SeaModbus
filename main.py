from CheckSum import CheckSum
from MessageGeneration import ReadMessageFunction
from ReadWriteMode import ReadWriteMode


def printRes(res):
    temp = []
    for item in res:
        temp.append(('%#.2X' % item)[2:])
    print(' '.join(temp))


if __name__ == '__main__':
    res = CheckSum.crc16([0x01, 0x01, 0x00, 0x00, 0x00, 0x0a])
    printRes(res)

    res = CheckSum.crc16([0x01, 0x01, 0x02, 0x02, 0x00])
    printRes(res)

    res = ReadMessageFunction.GetReadMessage(1, ReadWriteMode.ReadCoils, 0, 10)
    printRes(res)
