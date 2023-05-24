from src.MemAddress import MemAddress


class Memory:
    memory = []

    def __init__(self, count):
        for i in range(count):
            self.memory.append(MemAddress('mem' + str(i)))

    def gen_init(self):
        out = str()
        for mem in self.memory:
            out += mem.name + ': ' + mem.size + ' 0\n'
        return out
