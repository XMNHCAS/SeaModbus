from xmnhModbus.CheckSum import CheckSum
from xmnhModbus.MessageGeneration import ReadMessage, WriteMessage
from xmnhModbus.ReadWriteMode import ReadMode


def printRes(res):
    temp = []
    for item in res:
        temp.append(('%#.2X' % item)[2:])
    print(' '.join(temp))


if __name__ == '__main__':
    print('check sum:')
    printRes(CheckSum.crc16([0x01, 0x01, 0x00, 0x00, 0x00, 0x0a]))

    print('check sum:')
    printRes(CheckSum.crc16([0x01, 0x01, 0x02, 0x02, 0x00]))

    print('read message:')
    printRes(ReadMessage.GetReadMessage(1, ReadMode.ReadCoils, 0, 10))

    print('write single coil:')
    printRes(WriteMessage.WriteSingleCoilMessage(1, 1, True))

    print('write single register:')
    printRes(WriteMessage.WriteSingleRegisterMessage(1, 0, 300))

    print('write multiple coils')
    wValue = [False, False, False]
    for i in range(7):
        wValue.append(True)
    # print(WriteMessage.WriteMultipleCoilsMessage(1, 0, wValue))
    printRes(WriteMessage.WriteMultipleCoilsMessage(1, 0, wValue))

    print('write multiple registers')
    wValue = [10, 20, 30, 40, 50]
    printRes(WriteMessage.WriteMultipleRegistersMessage(1, 0, wValue))
