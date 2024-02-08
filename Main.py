import re
import sys
import math
from FileManagement import outputFileCreator, openFileLocation

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