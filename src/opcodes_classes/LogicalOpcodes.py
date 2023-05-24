from src.opcodes_classes.src_classes.Operand import Operand
from src.opcodes_classes.src_classes.Opcode import Opcode


class LogicalOpcodes:
    opcodes = [
        Opcode('I', 'ANDI', Operand.REGISTER, Operand.REGISTER, Operand.IMMEDIATE),
        Opcode('R', 'AND', Operand.REGISTER, Operand.REGISTER, Operand.REGISTER),
        Opcode('I', 'ORI', Operand.REGISTER, Operand.REGISTER, Operand.IMMEDIATE),
        Opcode('R', 'OR', Operand.REGISTER, Operand.REGISTER, Operand.REGISTER),
        Opcode('I', 'XORI', Operand.REGISTER, Operand.REGISTER, Operand.IMMEDIATE),
        Opcode('R', 'XOR', Operand.REGISTER, Operand.REGISTER, Operand.REGISTER)
    ]
