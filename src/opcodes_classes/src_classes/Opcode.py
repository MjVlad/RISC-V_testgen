class Opcode:
    def __init__(self, in_type, text, op1, op2, op3):
        self.in_type = in_type
        self.text = text
        self.ops = [op1, op2, op3]
        # self.op2 = op2
        # self.op3 = op3
