class Opcode:
    def __init__(self, in_type, text, op1, op2, op3, im_left=-2048, im_right=2047):
        self.in_type = in_type
        self.text = text
        self.ops = [op1, op2, op3]
        self.im_left = im_left
        self.im_right = im_right
