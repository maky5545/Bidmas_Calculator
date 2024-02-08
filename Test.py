import re

mathsList, reOrderedMathList = [], []
lineNumber, loopNumber = 1, 0
replaceListNum = float()
listLength = int()

userInput = input("Enter operation: ").rstrip()
userInput = userInput.replace(" ", "")
mathsList = re.split(r'(\+|-|\*|/)', userInput)
storedmathsList = mathsList
listLength = len(mathsList)
debugString = str()
for i in mathsList:
        debugString += i + ""

input(f"List Length: {listLength}")

input(f"\nMaths list:        {mathsList}")
input(f"Stored Maths List: {storedmathsList}")


def calcOperations(no1, no2, ariv):
        # Addition
        if ariv == "+":
                sum = no1 + no2
        elif ariv == "-":
                sum = no1 - no2
        elif ariv == "/":
                sum = no1 / no2
        elif ariv == "*":
                sum = no1 * no2
        return sum

def findListOperation(findOp, lst):
        firstNum, secondNum, operator, replaceListNum = 0, 0, str(), 0
        operationLoop = True

        while operationLoop == True:
                if findOp not in lst:
                        operationLoop = False
                else:
                        for i in range(len(lst) - 1, -1, -1):              
                                try:
                                        if lst[i] == findOp:
                                                operator = lst[i]
                                                firstNum = lst[i - 1]
                                                secondNum = lst[i + 1]
                                                input(f"First Num: {firstNum} Second Num: {secondNum} Operator: {operator}")
                                                replaceListNum = calcOperations(float(firstNum), float(secondNum), operator)
                                                lst[i - 1] = replaceListNum
                                                lst.pop(i)
                                                lst.pop(i)
                                                input(f"List: {lst}")
                                except IndexError:
                                        if len(lst) == 1:
                                                operationLoop = False
                                                input(f"List: {lst}")
                                                break

def calculate_expression(lst):
    for op in ["*", "/", "+", "-"]:
        findListOperation(op, lst)
    return lst[0]

calculate_expression(mathsList)

input(f"Final List: {mathsList}")
input(eval(debugString))