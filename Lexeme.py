from enum import Enum

class Lexeme:

    Type = ""
    Value = ""

    def __init__(self):
        Type = eLexemeType.Empty

class eLexemeType(Enum):
    Empty = 1
    Number = 2
    OpeningBracket = 3
    ClosingBracket = 4
    Operator = 5