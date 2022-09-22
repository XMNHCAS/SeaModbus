from enum import Enum


class ReadMode(Enum):
    ReadCoils = 0x01
    ReadDiscreteInputs = 0x02
    ReadHoldingRegisters = 0x03
    ReadInputRegisters = 0x04


class WriteMode(Enum):
    WriteSingleColis = 0x05
    WriteSingleRegister = 0x06
    WriteMultipleCoils = 0x15
    WriteMultipleRegisters = 0x16
