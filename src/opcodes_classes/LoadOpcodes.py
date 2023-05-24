from src.opcodes_classes.src_classes.Operand import Operand
from src.opcodes_classes.src_classes.Opcode import Opcode


class LoadOpcodes:
    opcodes = [
        # Opcode('I', 'LB', Operand.REGISTER, Operand.MEMORY, Operand.NOTHING),
        # Opcode('I', 'LBU', Operand.REGISTER, Operand.MEMORY, Operand.NOTHING),
        # Opcode('I', 'LH', Operand.REGISTER, Operand.MEMORY, Operand.NOTHING),
        # Opcode('I', 'LHU', Operand.REGISTER, Operand.MEMORY, Operand.NOTHING),
        Opcode('I', 'LW', Operand.REGISTER, Operand.MEMORY, Operand.NOTHING)#,
        # Opcode('I', 'LWU', Operand.REGISTER, Operand.MEMORY, Operand.NOTHING)
    ]
