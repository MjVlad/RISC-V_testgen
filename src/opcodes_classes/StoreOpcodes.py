from src.opcodes_classes.src_classes.Operand import Operand
from src.opcodes_classes.src_classes.Opcode import Opcode


class StoreOpcodes:
    opcodes = [
        # Opcode('S', 'SB', Operand.REGISTER, Operand.MEMORY, Operand.NOTHING),
        # Opcode('S', 'SH', Operand.REGISTER, Operand.MEMORY, Operand.NOTHING),
        Opcode('S', 'SW', Operand.REGISTER, Operand.MEMORY, Operand.NOTHING)
    ]
