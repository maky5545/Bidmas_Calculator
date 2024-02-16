from enum import Enum

class eLexemeType(Enum):
    Empty = 1
    Number = 2
    OpeningBracket = 3
    ClosingBracket = 4
    Plus = 5
    Minus = 6
    Times = 7
    Divide = 8

class Lexeme:

    Type = ""
    Value = ""
    NextLexeme = None
    AllowedNextLexemeTypes = []

    def __init__(self):
        self.Type = eLexemeType.Empty

class PlusLexeme(Lexeme):
    def __init__(self):
        self.Type = eLexemeType.Plus

        self.AllowedNextLexemeTypes = [
            eLexemeType.Number, 
            eLexemeType.OpeningBracket,
            eLexemeType.ClosingBracket]
    
class MinusLexeme(Lexeme):
    def __init__(self):
        self.Type = eLexemeType.Minus

        self.AllowedNextLexemeTypes = [
            eLexemeType.Number, 
            eLexemeType.OpeningBracket,
            eLexemeType.ClosingBracket]

class TimesLexeme(Lexeme):
    def __init__(self):
        self.Type = eLexemeType.Times

        self.AllowedNextLexemeTypes = [
            eLexemeType.Number, 
            eLexemeType.OpeningBracket,
            eLexemeType.ClosingBracket]

class DivideLexeme(Lexeme):
    def __init__(self):
        self.Type = eLexemeType.Divide

        self.AllowedNextLexemeTypes = [
            eLexemeType.Number, 
            eLexemeType.OpeningBracket,
            eLexemeType.ClosingBracket]

class NumberLexeme(Lexeme):
    def __init__(self):
        self.Type = eLexemeType.Number

        self.AllowedNextLexemeTypes = [
            eLexemeType.OpeningBracket,
            eLexemeType.ClosingBracket,
            eLexemeType.Plus,
            eLexemeType.Minus,
            eLexemeType.Times,
            eLexemeType.Divide]
    
class OpeningBracketLexeme(Lexeme):
    def __init__(self):
        self.Type = eLexemeType.OpeningBracket

        self.AllowedNextLexemeTypes = [
            eLexemeType.OpeningBracket,
            eLexemeType.ClosingBracket,
            eLexemeType.Number]
    
class ClosingBracketLexeme(Lexeme):
    def __init__(self):
        self.Type = eLexemeType.ClosingBracket

        self.AllowedNextLexemeTypes = [
            eLexemeType.OpeningBracket,
            eLexemeType.ClosingBracket,
            eLexemeType.Number]