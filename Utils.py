import os
import sys

def clear():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')