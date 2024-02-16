import re
import sys
import math
from FileManagement import outputFileCreator, openFileLocation
from Parser import Parser
from Sum import Sum

#<<<<< SY Test
parser = Parser

list = parser.ConvertToLexemes("122 +9/ (5 + 37* 6) ")

validationMessage = parser.Validate(list)

if validationMessage != "":
    print(validationMessage)
    exit()

sum = Sum
sum.BuildUp(list)

#for lexeme in list:
#    print("value = " + str(lexeme.Value))
#    print("type = " + str(lexeme.Type) + "\n")

#>>>>>
mathNumOps = []
toString = ""

userCalc = input("\n" + "Please input the calculation: ").rstrip()
mathNumOps = re.split(r'(\+|-|\*|/)', userCalc)  

for x in mathNumOps:
        toString += "" + x


print(toString)
lineCounter = 1
outputFileCreator(lineCounter, toString)
openFileLocation()
input("")