def newCalc(nums, ariv):
      nums = []
      toString = ""
      for x in nums:
        toString += " " + x
      pass

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

# Check if the number has a decimal part
def noDecimal(inoCheck):
    if inoCheck % 1 == 0:
        return True
    elif inoCheck % 1 != 0:
        return False
        
def convert_to_number(num):
        return int(num) if noDecimal(float(num)) else float(num)

# this sets the division to an integer if the answer is a whole number (this took me too long to work out. Probably rubbish code too)
def makeDivisionInt(answer):
       if noDecimal(answer) == True:
        answer = int(round(answer, 0))
        return answer
       else:
             answer = answer
             return answer