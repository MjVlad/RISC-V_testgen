from src.opcodes_classes.src_classes.Operand import Operand
from src.opcodes_classes.src_classes.Opcode import Opcode


class MiscellaneousOpcodes:
    opcodes = [
        Opcode('', 'LI', Operand.REGISTER, Operand.IMMEDIATE, Operand.NOTHING),
        Opcode('', 'LA', Operand.REGISTER, Operand.MEMORY, Operand.NOTHING),
        Opcode('R', 'SLT', Operand.REGISTER, Operand.REGISTER, Operand.REGISTER),
        Opcode('I', 'SLTI', Operand.REGISTER, Operand.REGISTER, Operand.IMMEDIATE),
        Opcode('R', 'SGT', Operand.REGISTER, Operand.REGISTER, Operand.REGISTER),
        Opcode('R', 'SLTU', Operand.REGISTER, Operand.REGISTER, Operand.REGISTER),
        Opcode('I', 'SLTIU', Operand.REGISTER, Operand.REGISTER, Operand.IMMEDIATE),
        Opcode('R', 'SGTU', Operand.REGISTER, Operand.REGISTER, Operand.REGISTER),
        Opcode('', 'SEQZ', Operand.REGISTER, Operand.REGISTER, Operand.NOTHING),
        Opcode('', 'SNEZ', Operand.REGISTER, Operand.REGISTER, Operand.NOTHING),
    ]
