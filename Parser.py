from Lexeme import Lexeme
from Lexeme import eLexemeType

class Parser:

    intIndex = 0

    def __init__(self):
        self.data = []

    @classmethod
    def ConvertToLexemes(self, strInput):
        
        lstLexemes = []
        strInput = str(strInput)

        self.intIndex = 0

        while  self.intIndex < len(strInput):
            lexeme = self.__ConvertToLexeme(self, strInput)
            
            if lexeme.Type != eLexemeType.Empty:
                lstLexemes.append(lexeme)

            self.intIndex += 1

        return lstLexemes

    def __ConvertToLexeme(self, strInput):

        value = self.__GetValue(self, strInput)
        
        lexeme = Lexeme()
        lexeme.Value = ""

        if value.isdigit():
            lexeme.Type = eLexemeType.Number
            lexeme.Value = value
        elif value == "+":
            lexeme.Type = eLexemeType.Operator
        elif value == "-":
            lexeme.Type = eLexemeType.Operator
        elif value == "*":
            lexeme.Type = eLexemeType.Operator
        elif value == "/":
            lexeme.Type = eLexemeType.Operator
        elif value == "(":
            lexeme.Type = eLexemeType.OpeningBracket
        elif value == ")":
            lexeme.Type = eLexemeType.ClosingBracket
        else:
            lexeme.Type = eLexemeType.Empty

        return lexeme

    def __GetValue(self, strInput, priorValue = ""):

        if len(strInput) <= self.intIndex:
            return priorValue
        
        value = str(strInput)[self.intIndex]

        if value.isdigit():
            value = priorValue + value
            if self.__NextCharacterAlongIsADigit(self, strInput):
                self.intIndex += 1
                return str(self.__GetValue(self, strInput, value))

        return value
    
    def __NextCharacterAlongIsADigit(self, strInput):
        if len(strInput) <= (self.intIndex + 1):
            return False
        nextValue = str(strInput)[self.intIndex + 1]
        return nextValue.isdigit()