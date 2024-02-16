from Lexeme import (
    eLexemeType, 
    Lexeme, 
    PlusLexeme, 
    MinusLexeme, 
    TimesLexeme, 
    DivideLexeme, 
    NumberLexeme, 
    OpeningBracketLexeme, 
    ClosingBracketLexeme)

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
            lexeme = self.__ConvertToLexeme(strInput)

            if lexeme.Type != eLexemeType.Empty:
                lstLexemes.append(lexeme)

            self.intIndex += 1

        return lstLexemes

    @classmethod
    def Validate(self, lstLexemes):

        matchingNumberOfBrackets, bracketsInWrongOrder = self.__ValidateBrackets(lstLexemes)

        if matchingNumberOfBrackets == False:
            return "Number of opening and closing brackets doesn't match"

        if bracketsInWrongOrder == True:
            return "Closing bracket before opening bracket"

        orderErrorFound, orderErrorMessage = self.__ValidateLexemeOrder(lstLexemes)
        if orderErrorFound == True:
            return orderErrorMessage
            
        return "no errors" #change to "" once happy all working

    def __LinkLexemes(lstLexemes):
        for intIndex in range(0, len(lstLexemes) - 1):
            lstLexemes[intIndex].NextLexeme = lstLexemes[intIndex + 1]
        return lstLexemes
    
    @classmethod
    def __ValidateLexemeOrder(self, lstLexemes):

        lstLexemes = self.__LinkLexemes(lstLexemes)

        for l in lstLexemes:
            if l.NextLexeme != None:
                if l.NextLexeme.Type not in l.AllowedNextLexemeTypes:
                    return True, l.NextLexeme.Type.name + " not allowed after " + l.Type.name
        return False, ""

    def __ValidateBrackets(lstLexemes):
        
        openingBracketCount = 0
        closingBracketCount = 0
        bracketsInWrongOrder = False
        
        for lexeme in lstLexemes:
            openingBracketCount += 1 if lexeme.Type == eLexemeType.OpeningBracket else 0
            closingBracketCount += 1 if lexeme.Type == eLexemeType.ClosingBracket else 0
            bracketsInWrongOrder = True if closingBracketCount > openingBracketCount else bracketsInWrongOrder

        matchingNumberOfBrackets = openingBracketCount == closingBracketCount
        
        return matchingNumberOfBrackets, bracketsInWrongOrder

    @classmethod
    def __ConvertToLexeme(self, strInput):

        value = self.__GetValue(strInput)

        if value.isdigit():
            numberLexeme = NumberLexeme()
            numberLexeme.Value = value
            return numberLexeme
        elif value == "+":
            return PlusLexeme()
        elif value == "-":
            return MinusLexeme()
        elif value == "*":
            return TimesLexeme()
        elif value == "/":
            return DivideLexeme()
        elif value == "(":
            return OpeningBracketLexeme()
        elif value == ")":
            return ClosingBracketLexeme()
        else:
            return Lexeme()

    @classmethod
    def __GetValue(self, strInput, priorValue = ""):

        if len(strInput) <= self.intIndex:
            return priorValue
        
        value = str(strInput)[self.intIndex]

        if value.isdigit():
            value = priorValue + value
            if self.__NextCharacterAlongIsADigit(strInput):
                self.intIndex += 1
                return str(self.__GetValue(strInput, value))

        return value
    
    @classmethod
    def __NextCharacterAlongIsADigit(self, strInput):
        if len(strInput) <= (self.intIndex + 1):
            return False
        nextValue = str(strInput)[self.intIndex + 1]
        return nextValue.isdigit()