

class MemAddress:  #TODO сделать возможность работать с массивами
    def __init__(self, name, size='.word', is_arr=False):
        self.name = name
        self.size = size
        self.is_arr = is_arr
