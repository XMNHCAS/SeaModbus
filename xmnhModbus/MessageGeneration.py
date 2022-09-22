from xmnhModbus.CheckSum import CheckSum
from xmnhModbus.ReadWriteMode import ReadMode
from xmnhModbus.ReadWriteMode import WriteMode


class ReadMessage:
    '''
    Read message generation class

    读取报文生成类
    '''

    def GetReadMessage(slaveID: int, readType: ReadMode, startAddr: int,
                       length: int) -> list[int]:
        '''
        Get read message

        获取读取报文

        Args:
            slaveID (int): Slave address (从站地址)
            readType (ReadMode): Read Mode (读取模式)
            startAddr (int): Start address (起始地址)
            length (int): Read quantity (读取数量)

        Returns:
            list[int]: Generated read message array (生成的读取报文数组)
        '''
        id = int.to_bytes(slaveID, 1, 'big')
        rType = int.to_bytes(readType.value, 1, 'big')
        start = int.to_bytes(startAddr, 2, 'big')
        readLen = int.to_bytes(length, 2, 'big')
        res = [id[0], rType[0], start[0], start[1], readLen[0], readLen[1]]

        # 计算CRC16校验码
        checks = CheckSum.crc16(res)
        for item in checks:
            res.append(item)
        return res


class WriteMessage:
    '''
    Write message generation class

    写入报文生成类
    '''

    def __getMessageHeader(slaveID: int, startAddr: int,
                           mode: WriteMode) -> list[int]:
        '''
        获取起始报文

        Args:
            slaveID (int): Slave address (从站地址)
            startAddr (int): Start address (起始地址)
            mode (WriteMode): Write Mode (读取模式)

        Returns:
            list[int]: Generated starting  message array (生成的起始报文数组)
        '''
        id = int.to_bytes(slaveID, 1, 'big')
        wType = int.to_bytes(mode.value, 1, 'big')
        start = int.to_bytes(startAddr, 2, 'big')
        return [id[0], wType[0], start[0], start[1]]

    def __convertBooleanArrayToByte(arr: list[bool]) -> int:
        '''
        Generate corresponding bytes according to the input Boolean list

        根据输入的布尔集合生成对应的字节

        Args:
            arr (list[bool]): The input Boolean list (输入的布尔量集合)

        Returns:
            int: Result of conversion (转换的结果)
        '''
        index = len(arr)
        res = 0x00

        while index > 0:
            index = index - 1
            if arr[index]:
                res = res | 0x01 << index

        return res

    def __calcCheckSum(res: list) -> list:
        '''
        Calculate the check sum according to the generated message and return complete messages

        根据已生成的报文计算其校验码，并返回全部完整的报文

        Args:
            res (list): The generated message (已生成的报文)

        Returns:
            list: The complete messages (最终的完整报文)
        '''
        temp = res
        checks = CheckSum.crc16(res)
        for item in checks:
            temp.append(item)
        return temp

    def WriteSingleCoilMessage(slaveID: int, startAddr: int,
                               value: bool) -> list:
        '''
        Generate the message will use to write to a single coil

        生成写入单个线圈的报文

        Args:
            slaveID (int): Slave address (从站地址)
            startAddr (int): Start address (起始地址)
            value (bool): (线圈写入值)

        Returns:
            list: (生成的报文)
        '''
        res = WriteMessage.__getMessageHeader(slaveID, startAddr,
                                              WriteMode.WriteSingleCoil)
        vByte = int.to_bytes(0xff, 2, 'little')
        if (value is not True):
            vByte = int.to_bytes(0x00, 2, 'little')

        res.append(vByte[0])
        res.append(vByte[1])

        return WriteMessage.__calcCheckSum(res)

    def WriteSingleRegisterMessage(slaveID: int, startAddr: int,
                                   value: int) -> list:
        '''
        Generate the message will use to write to a single register

        生成写入单个寄存器的报文

        Args:
            slaveID (int): Slave address (从站地址)
            startAddr (int): Start address (起始地址)
            value (int): (寄存器写入值)

        Returns:
            list: (生成的报文)
        '''
        res = WriteMessage.__getMessageHeader(slaveID, startAddr,
                                              WriteMode.WriteSingleRegister)
        vByte = int.to_bytes(value, 2, 'big')

        res.append(vByte[0])
        res.append(vByte[1])

        return WriteMessage.__calcCheckSum(res)

    def WriteMultipleCoilsMessage(slaveID: int, startAddr: int,
                                  value: list[bool]) -> list:
        '''
        Generate the message will use to write to multiple coils

        生成批量写入线圈的报文

        Args:
            slaveID (int): Slave address (从站地址)
            startAddr (int): Start address (起始地址)
            value (list[bool]): (批量写入的值)

        Returns:
            list: (生成的报文)
        '''
        res = WriteMessage.__getMessageHeader(slaveID, startAddr,
                                              WriteMode.WriteMultipleCoils)
        coilsCount = int.to_bytes(len(value), 2, 'big')
        res.append(coilsCount[0])
        res.append(coilsCount[1])

        res.append(int(len(value) / 8) + 1)

        index = 0
        while index < len(value):
            tempArr = []
            if index + 8 < len(value):
                tempArr = value[index:index + 8]
            else:
                tempArr = value[index:]
            res.append(WriteMessage.__convertBooleanArrayToByte(tempArr))
            index = index + 8

        return WriteMessage.__calcCheckSum(res)

    def WriteMultipleRegistersMessage(slaveID: int, startAddr: int,
                                      value: list[int]) -> list:
        '''
        Generate the message will use to write to multiple registers

        生成批量写入寄存器的报文

        Args:
            slaveID (int): Slave address (从站地址)
            startAddr (int): Start address (起始地址)
            value (list[int]): (批量写入的值)

        Returns:
            list: (生成的报文)
        '''
        res = WriteMessage.__getMessageHeader(slaveID, startAddr,
                                              WriteMode.WriteMultipleRegisters)
        registersCount = int.to_bytes(len(value), 2, 'big')

        res.append(registersCount[0])
        res.append(registersCount[1])

        res.append(len(value) * 2)

        for i in range(len(value)):
            temp = int.to_bytes(value[i], 2, 'big')
            res.append(temp[0])
            res.append(temp[1])

        return WriteMessage.__calcCheckSum(res)
