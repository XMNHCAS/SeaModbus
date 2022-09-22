from xmnhModbus.CheckSum import CheckSum
from xmnhModbus.MessageGeneration import ReadMessage, WriteMessage
from xmnhModbus.ReadWriteMode import ReadMode


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

    res = ReadMessage.GetReadMessage(1, ReadMode.ReadCoils, 0, 10)
    printRes(res)

    printRes(WriteMessage.WriteSingleColisMessage(1, 1, True))
