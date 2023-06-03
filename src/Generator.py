import random

from src.Line import Line
from src.Memory import Memory
from src.Registers import Registers
from src.Opcodes import Opcodes
from src.opcodes_classes.src_classes.Opcode import Opcode
from src.opcodes_classes.src_classes.Operand import Operand


class Generator:
    memory = Memory(10)

    # def __init__(self):

    @staticmethod
    def chose_reg():  # TODO сделать зависимости от кол-ва чтений и записи в регистр
        return Registers.registers[random.randint(5, 31)]

    @staticmethod
    def chose_opcode():  # TODO сделать зависимость от весового коэффициента инструкции
        op_group = Opcodes.opcodes[random.randint(0, len(Opcodes.opcodes) - 1)]
        return op_group.opcodes[random.randint(0, len(op_group.opcodes) - 1)]

    def chose_mem(self):  # TODO сделать учитывание размера ячейки
        return self.memory.memory[random.randint(0, len(self.memory.memory) - 1)]

    def gen_la(self):
        line = Line()
        line.set_opcode('LA')
        line.set_operand('ra')
        line.set_operand(self.chose_mem().name)
        return line

    def gen_instruction(self):  # TODO использовать метки
        line = Line()
        opcode = self.chose_opcode()
        line.set_opcode(opcode.text)
        for i, op in enumerate(opcode.ops):
            if op == Operand.IMMEDIATE:
                line.set_operand(str(random.randint(opcode.im_left, opcode.im_right)))  # TODO учитывать размер immediate
            if op == Operand.REGISTER:
                reg = self.chose_reg()
                if (opcode.in_type == 'I' or opcode.in_type == 'R' or opcode.in_type == 'U') and i == 0:
                    reg.s_count += 1
                elif reg.s_count == 0:
                    line = Line()
                    line.set_opcode('NOP')
                    break
                line.set_operand(reg.name)
            if op == Operand.MEMORY:
                line.set_operand(self.chose_mem().name)
            if op == Operand.NOTHING:
                break
        return line

    def gen_instructions(self, count):
        out_str = str()
        i = 0
        while i < count:
            line = self.gen_instruction()
            if line.get_opcode() == 'NOP':
                continue
            if line.get_opcode() == 'SW':
                out_str += self.gen_la().get_line() + '\n'
                line.change_last_op('ra')
                i += 1
            out_str += line.get_line() + '\n'
            i += 1
        return out_str

    def gen_header(self):
        header = '#include "riscv_test.h"\n\nRVTEST_RV32U\nRVTEST_CODE_BEGIN\n\n' \
                 '\tj test_start\n\ncrash_backward:\n\tRVTEST_FAIL\n\ntest_start:\n'
        return header

    def xreg_init(self):
        out = '\tli x0, 0\n'
        for i in range(1, 32):
            out += f'\tli x{i}, 0\n'
        return out

    def gen_dump(self):
        out = '\tla x1, xreg_output_data\n\tsw x0, 0(x1)\n'
        mem_offset = 4
        for i in range(2, 32):
            out += f'\tsw x{i}, {mem_offset}(x1)\n'
            mem_offset += 4
        return out

    def gen_output_data(self):
        out = str()
        for i in range(32):
            out += f'\treg_x{i}_output:	.word 0\n'
        return out

    def gen_code(self, number_instruction):
        return self.gen_header() + 'xreg_init:\n' + self.xreg_init() + \
            '\tj pseg_0\n\npseg_0:\n' + self.gen_instructions(number_instruction) + \
            '\tj reg_dump\n\nreg_dump:\n' + self.gen_dump() + '\n\tj test_end\n\n' \
            'crash_forward:\n\tRVTEST_FAIL\n\ntest_end:\n\tRVTEST_PASS\n\n' \
            'RVTEST_CODE_END\n\n.data\n' + self.memory.gen_init() + '\nRVTEST_DATA_BEGIN\n\n' \
            'xreg_output_data:\n' + self.gen_output_data() + '\nRVTEST_DATA_END\n'
