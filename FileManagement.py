import os
import subprocess
from datetime import datetime
from Misc import consoleSleep2

userName = os.getlogin()
dateAndTime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
calcFileDirec = (os.path.dirname(os.path.abspath(__file__)))
checkDirecExists = os.path.isdir(calcFileDirec)
calcFileDirec = calcFileDirec + "\\Files\\"
fileName = f"calc_{dateAndTime}.txt"
checkFileExists = os.path.isfile(f"{calcFileDirec}{fileName}")
tryMakeDir = 0
tryFindDir = 0
testLoop = 0

# Create Log Files and write output to them
def outputFileCreator(lineCounter, value):
    global tryMakeDir
    global createFile
    global tryFindDir
    
    if checkDirecExists == False:
        while True:
            try:
                os.makedirs(calcFileDirec, 0o777, exist_ok=False)
                break                
            except FileExistsError:
                if tryMakeDir < 3:
                    print("Code Failed: directory already exists! Trying again...")
                    tryMakeDir += 1
                    consoleSleep2()
                else:
                    print("Code Failed: directory already exists! Exiting...")
                    consoleSleep2()
                    exit()
                            
    else:
        while True:
                createFile = open(f"{calcFileDirec}\\{fileName}", "a")
                createFile.write(f"{lineCounter}. {value} \n\n")
                createFile.close()
                break

def fileLocation():
    print("\nA calculation files with all of the equations and answers has"
       " been created here:")
    print("\033[92m" + f"{calcFileDirec}{fileName}" + "\033[0m")

def openFileLocation():
    subprocess.Popen(f'explorer "{calcFileDirec}"')
