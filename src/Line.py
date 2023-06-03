

class Line:
    __label = str()
    __opcode = str()
    __ops = str()

    def set_label(self, label):
        self.__label = label + ':'

    def set_opcode(self, opcode):
        self.__opcode = opcode

    def set_operands(self, operands):
        self.__ops = operands[0]
        for op in operands[1:]:
            self.__ops += ', ' + op

    def set_operand(self, operand):
        if len(self.__ops) == 0:
            self.__ops = operand
        else:
            self.__ops += ', ' + operand

    def change_last_op(self, operand):
        ins = [pos for pos, char in enumerate(self.__ops) if char == ',']
        if ins[-1] != -1:
            self.__ops = self.__ops[0:ins[-1]]
        self.set_operand(operand)


    def get_opcode(self):
        return self.__opcode

    def get_line(self):
        return self.__label + '\t' + self.__opcode + '\t' + self.__ops
