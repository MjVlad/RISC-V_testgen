from src.opcodes_classes.src_classes.Operand import Operand
from src.opcodes_classes.src_classes.Opcode import Opcode


class ShiftingOpcodes:
    opcodes = [
        Opcode('I', 'SLLI', Operand.REGISTER, Operand.REGISTER, Operand.IMMEDIATE, 0, 31),
        # Opcode('R', 'SLL', Operand.REGISTER, Operand.REGISTER, Operand.REGISTER),
        Opcode('I', 'SRLI', Operand.REGISTER, Operand.REGISTER, Operand.IMMEDIATE, 0, 31),
        # Opcode('R', 'SRL', Operand.REGISTER, Operand.REGISTER, Operand.REGISTER),
        Opcode('I', 'SRAI', Operand.REGISTER, Operand.REGISTER, Operand.IMMEDIATE, 0, 31)
        # Opcode('R', 'SRA', Operand.REGISTER, Operand.REGISTER, Operand.REGISTER)
    ]
