# Imports
import os
import time

# clears the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# sleeps the console for 2 seconds
def consoleSleep2():
    time.sleep(2)