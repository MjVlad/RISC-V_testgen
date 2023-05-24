from enum import Enum

class Operand(Enum):
    NOTHING = 0
    REGISTER = 1
    IMMEDIATE = 2
    MEMORY = 3
