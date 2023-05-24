from src.opcodes_classes.src_classes.Operand import Operand
from src.opcodes_classes.src_classes.Opcode import Opcode


class ArithmeticOpcodes:
    opcodes = [
        Opcode('I', 'ADDI', Operand.REGISTER, Operand.REGISTER, Operand.IMMEDIATE),
        # Opcode('I', 'ADDIW', Operand.REGISTER, Operand.REGISTER, Operand.IMMEDIATE),
        Opcode('R', 'ADD', Operand.REGISTER, Operand.REGISTER, Operand.REGISTER),
        # Opcode('R', 'ADDW', Operand.REGISTER, Operand.REGISTER, Operand.REGISTER),
        Opcode('R', 'SUB', Operand.REGISTER, Operand.REGISTER, Operand.REGISTER),
        # Opcode('R', 'SUBW', Operand.REGISTER, Operand.REGISTER, Operand.REGISTER)
    ]
