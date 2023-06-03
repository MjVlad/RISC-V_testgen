from src.opcodes_classes.ArithmeticOpcodes import ArithmeticOpcodes
from src.opcodes_classes.LoadOpcodes import LoadOpcodes
from src.opcodes_classes.LogicalOpcodes import LogicalOpcodes
from src.opcodes_classes.MiscellaneousOpcodes import MiscellaneousOpcodes
from src.opcodes_classes.ShiftingOpcodes import ShiftingOpcodes
from src.opcodes_classes.StoreOpcodes import StoreOpcodes


class Opcodes:
    opcodes = [
        ArithmeticOpcodes(),
        LoadOpcodes(),
        LogicalOpcodes(),
        MiscellaneousOpcodes(),
        ShiftingOpcodes(),
        StoreOpcodes()
    ]
