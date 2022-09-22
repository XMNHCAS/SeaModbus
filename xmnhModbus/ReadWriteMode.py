from enum import Enum


class ReadMode(Enum):
    '''
    Read mode

    读取模式

    Args:
        Enum (_type_): Type of enumeration (枚举类型)
    '''
    ReadCoils = 0x01
    ReadDiscreteInputs = 0x02
    ReadHoldingRegisters = 0x03
    ReadInputRegisters = 0x04


class WriteMode(Enum):
    '''
    Write mode

    写入模式

    Args:
        Enum (_type_): Type of enumeration (枚举类型)
    '''
    WriteSingleCoil = 0x05
    WriteSingleRegister = 0x06
    WriteMultipleCoils = 0x0f
    WriteMultipleRegisters = 0x10
